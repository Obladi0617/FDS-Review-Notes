<!-- Slide number: 1 -->
CHAPTER  8
THE DISJOINT SET ADT
§1  Equivalence Relations
【Definition】A relation R is defined on a set S if for every pair of elements (a, b), a, b S, a R b is either true or false.  If a R b is true, then we say that a is related to b.
【Definition】A relation, ~, over a set, S, is said to be an equivalence relation over S iff it is symmetric, reflexive, and transitive over S.
【Definition】Two members x and y of a set S are said to be in the same equivalence class iff x ~ y.
1/9

<!-- Slide number: 2 -->
§2  The Dynamic Equivalence Problem

![DARTS](Picture1516.jpg)
Given an equivalence relation ~, decide for any a and b if a ~ b.
〖Example〗  Given  S = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 } and 9 relations: 124, 31, 610, 89, 74, 68, 35, 211, 1112.
    The equivalence classes are  { 2, 4, 7, 11, 12 }, { 1, 3, 5 }, { 6, 8, 9, 10 }
Algorithm:
{   /* step 1: read the relations in */
    Initialize N disjoint sets;
    while ( read in a ~ b ) {
        if ( ! (Find(a) == Find(b)) )
	Union the two sets;
    } /* end-while */
    /* step 2: decide if a ~ b */
    while ( read in a and b )
        if ( Find(a) == Find(b) )   output( true );
        else   output( false );
}
(Union / Find)
Dynamic (on-line)
2/9

<!-- Slide number: 3 -->
§2 The Dynamic Equivalence Problem
 Elements of the sets:  1, 2, 3, ..., N
 Sets :  S1, S2, ... ...  and  Si  Sj =  ( if  i  j ) —— disjoint
〖Example〗  S1 = { 6, 7, 8, 10 }, S2 = { 1, 4, 9 }, S3 = { 2, 3, 5 }
Note:
Pointers are
from children
to parents
10

6
8
7
4

1
9
2

3
5
A possible forest representation of these sets
 Operations :
(1)  Union( i, j ) ::= Replace Si and Sj by S = Si  Sj
(2)  Find( i ) ::= Find the set Sk which contains the element i.
3/9

<!-- Slide number: 4 -->
§3  Basic Data Structure
  Union ( i, j )
Idea:  Make Si a subtree of Sj , or vice versa.  That is, we can set the parent pointer of one of the roots to the other root.
10

6
8
7
4

1
9

10

6
8
7
4

1
9
S1  S2
S2  S1
Implementation 1:
10

6
8
7

4

1
9

2

3
5

S1

name[ ]
S2

S3

S2  S1
   S2
4/9

<!-- Slide number: 5 -->
§3  Basic Data Structure
Implementation 2:  S [ element ] = the element’s parent.
Note:  S [ root ] = 0  and  set name = root index.
〖Example〗The array representation of the three sets is
Here we use the fact that
the elements are numbered from 1 to N.
Hence they can be used as
indices of an array.
[1]
4
[2]
0
[3]
2
[4]
0
[5]
2
[6]
10
[7]
10
[8]
10
[9]
4
[10]
0
S
10

6
8
7
4

1
9
2

3
5

10

void  SetUnion ( DisjSet S,
                             SetType Rt1,
                             SetType Rt2 )
{    S [ Rt2 ] = Rt1 ;     }
( S1  S2     S1 )    S [ 4 ] = 10
  Find ( i )
Implementation 1:
Implementation 2:

j

name[k]
S


...
i

SetType  Find ( ElementType X,
                           DisjSet S )
{   for ( ; S[X] > 0; X = S[X] )   ;
    return  X ;
}

find ( i ) =
‘S’
5/9

<!-- Slide number: 6 -->
§3  Basic Data Structure
  Analysis

N

N1



1
T = ( N2 ) !
That’s not
good.
Practically speaking, union and find are always paired. Thus we consider the performance of a sequence of union-find operations.
Sure.  Try this one:
union(2, 1), find(1);
union(3, 2), find(1);
..., ... ;
  union(N, N 1), find(1).
        Can you think of
  a worst case example?

〖Example〗  Given  S = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 } and 9 relations: 124, 31, 610, 89, 74, 68, 35, 211, 1112.   We have 3 equivalence classes { 2, 4, 7, 11, 12 }, { 1, 3, 5 }, and { 6, 8, 9, 10 }

Algorithm using union-find operations
{  Initialize  Si = { i }  for  i = 1, ..., 12 ;
   for  ( k = 1; k <= 9; k++ )  {  /* for each pair  i  j */
      if  ( Find( i ) != Find( j ) )
          SetUnion( Find( i ), Find( j ) );
   }
}

6/9

<!-- Slide number: 7 -->
§4  Smart Union Algorithms
  Union-by-Size
-- Always change the smaller tree
S [ Root ] = – size;  /* initialized to be –1 */
【Lemma】Let T be a tree created by union-by-size with N nodes, then
Now T = O( N )
for the worst case
example I gave.

1

2
N

Proof:  By induction.  (Each element can have its set name changed at most log2 N times.)
Time complexity of  N  Union and M Find operations is now O( N + M log2 N ).
  Union-by-Height
-- Always change the shallow tree

Please read Figure 8.13 on p.273 for detailed implementation.
7/9

<!-- Slide number: 8 -->
§5  Path Compression
SetType  Find ( ElementType  X, DisjSet  S )
{
    if ( S[ X ] <= 0 )    return  X;
    else    return  S[ X ] = Find( S[ X ], S );
}

Slower for
a single find, but
faster for a sequence of
find operations.
SetType  Find ( ElementType  X, DisjSet  S )
{   ElementType  root,  trail,  lead;
    for ( root = X; S[ root ] > 0; root = S[ root ] )
        ;  /* find the root */
    for ( trail = X; trail != root; trail = lead ) {
       lead = S[ trail ] ;
       S[ trail ] = root ;
    }  /* collapsing */
    return  root ;
}
Note: Not compatible with union-by-height since it changes the heights.  Just take “height” as an estimated rank.
8/9

<!-- Slide number: 9 -->
§6  Worst Case for
         Union-by-Rank and Path Compression
【Lemma (Tarjan)】Let T( M, N ) be the maximum time required to process an intermixed sequence of M  N finds and N  1 unions.  Then:
k1M  ( M, N )  T( M, N )  k2M  ( M, N )
     for some positive constants k1 and k2 .
log* 265536 = 5 since logloglogloglog ( 265536 )= 1
 Ackermann’s Function and  ( M, N )

http://mathworld.wolfram.com/AckermannFunction.html
 O( log* N )   4
log* N (inverse Ackermann function)
  = # of times the logarithm is applied to N until the result  1.
9/9

<!-- Slide number: 10 -->
Bonus Problem 2

 Social Clusters
(2 points)
Due:  Sunday, January 17th, 2020 at 10:00pm
The problem can be found and submitted at
 https://pintia.cn/