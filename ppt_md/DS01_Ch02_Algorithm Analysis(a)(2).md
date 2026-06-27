<!-- Slide number: 1 -->
CHAPTER  2
ALGORITHM ANALYSIS
【Definition】An algorithm is a finite set of instructions that, if followed, accomplishes a particular task.   In addition,  all algorithms must satisfy the following criteria:
(1)   Input    There are zero or more quantities that are externally supplied.
(2)   Output    At least one quantity is produced.
(3)   Definiteness    Each instruction is clear and unambiguous.
(4)   Finiteness    If we trace out the instructions of an algorithm, then for all cases, the algorithm terminates after finite number of steps.
(5)   Effectiveness    Every instruction must be basic enough to be carried out, in principle, by a person using only pencil and paper.  It is not enough that each operation be definite as in(3); it also must be feasible.
1/15

<!-- Slide number: 2 -->
Note: A program is written in some programming language, and does not have to be finite (e.g. an operation system).
           An algorithm can be described by human languages, flow charts, some programming languages, or pseudo-code.
〖Example〗 Selection Sort:  Sort a set of n  1 integers in increasing order.
From those integers that are currently unsorted, find the smallest and place it next in the sorted list.

 Where and how
   are they stored?

for ( i = 0; i < n; i++) {
    Examine list[i] to list[n1] and suppose that the smallest integer is at list[min];
  Interchange list[i] and list[min];
}
  Where?
  Algorithm  in
   pseudo-code
Sort = Find the smallest integer + Interchange it with list[i].
2/15

<!-- Slide number: 3 -->
§1   What to Analyze
 Machine & compiler-dependent run times.
 Time & space complexities : machine & compiler-independent.

 Assumptions:
  instructions are executed sequentially
  each instruction is simple, and takes exactly one time unit
  integer size is fixed and we have infinite memory
Typically the following two functions are analyzed:
   Tavg(N) & Tworst(N)  --  the average and worst case time complexities, respectively, as functions of input size N.

If there is more than one input, these functions may have more than one argument.
3/15

<!-- Slide number: 4 -->
§1  What to Analyze
〖Example〗 Matrix addition

void  add ( int  a[ ][ MAX_SIZE ],
                   int  b[ ][ MAX_SIZE ],
                   int  c[ ][ MAX_SIZE ],
                   int  rows,  int  cols )
{
    int  i,  j ;
    for ( i = 0; i < rows; i++ )
          for ( j = 0; j < cols; j++ )
                c[ i ][ j ] = a[ i ][ j ] + b[ i ][ j ];
}
Q: What shall we do
 if rows >> cols?
A: Exchange
rows and cols.

/* rows + 1 */
/* rows(cols+1) */
/* rows  cols */
T(rows, cols ) =  2 rows  cols + 2rows + 1
4/15

<!-- Slide number: 5 -->
§1  What to Analyze

float  sum ( float  list[ ],  int  n )
{  /* add a list of numbers */
   float  tempsum = 0;
   int  i ;
   for ( i = 0; i < n; i++ )

       tempsum  += list [ i ] ;

   return  tempsum;
}
〖Example〗Iterative function for summing a list of numbers
/* count = 1 */
/* count ++ */
/* count ++ */
Tsum ( n ) = 2n + 3
/* count ++ for last execution of for */
/* count ++ */
〖Example〗Recursive function for summing a list of numbers

float  rsum ( float  list[ ],  int  n )
{  /* add a list of numbers */
   if ( n )
       return rsum(list, n1) + list[n  1];

   return   0;
}
/* count ++ */
Trsum ( n ) = 2n + 2
But it takes more time to compute each step.
/* count ++ */
/* count ++ */
5/15

<!-- Slide number: 6 -->
§1  What to Analyze
Take the iterative and
recursive programs for summing
a list for example --- if you think 2n+2 is
less than 2n+3, try a large n and
you’ll be surprised !
Good question !
Let’s ask the students ...
          I see ...
Then what’s the point of
this Tp stuff?
          So it’s too complicated sometimes.
But does it worth the effort?
        Is it really necessary
to count the exact
number of steps ?
Uhhh ...
 I don’t think so.
Because
 it drives me crazy!
Why not?

6/15

<!-- Slide number: 7 -->
§2   Asymptotic Notation  ( , , , o )
The point of counting the steps is to predict the growth in run time as the N change, and thereby compare the time complexities of two programs.  So what we really want to know is the asymptotic behavior of Tp.

![](Picture5.jpg)
Suppose Tp1 ( N ) = c1N2 + c2N and Tp2 ( N ) = c3N.  Which one is faster?
No matter what  c1, c2, and c3 are, there will be an n0 such that Tp1 ( N ) > Tp2 ( N ) for all N > n0.

I see!  So as long as I know that
Tp1 is about N2 and Tp2 is about N, then for
sufficiently large N,  P2 will be faster!

7/15

<!-- Slide number: 8 -->
§2  Asymptotic Notation
【Definition】  T (N) = O( f (N) ) if there are positive constants c and n0 such that  T (N)  c  f (N) for all N  n0.
【Definition】  T (N) = ( g(N) ) if there are positive constants c and n0 such that  T (N)  c  g(N) for all N  n0.
【Definition】  T (N) = ( h(N) ) if and only if T (N) = O( h(N) ) and T (N) = ( h(N) ) .
【Definition】  T (N) = o( p(N) ) if T (N) = O( p(N) ) and T (N)  ( p(N) ) .
Note:
  2N + 3 = O( N ) = O( Nk1 ) = O( 2N ) =   We shall always take the smallest f (N).
  2N + N2 = ( 2N ) = ( N2 ) = ( N ) = ( 1 ) =    We shall always take the largest g(N).
8/15

<!-- Slide number: 9 -->
§2  Asymptotic Notation

![](Picture5.jpg)
Rules of Asymptotic Notation
 If T1 (N) = O( f (N) ) and T2 (N) = O( g(N) ), then
	(a) T1 (N) + T2 (N) = max( O( f (N)), O( g(N)) ),
	(b) T1 (N) * T2 (N) = O( f (N) * g(N) ).
 If T (N) is a polynomial of degree k, then T (N) = ( N k ).
 logk N = O(N) for any constant k.  This tells us that logarithms grow very slowly.
Note:  When compare the complexities of two programs asymptotically, make sure that N is sufficiently large.
    For example, suppose that Tp1 ( N ) = 106N and Tp2 ( N ) = N2.  Although it seems that ( N2 ) grows faster than ( N ), but if N < 106,  P2 is still faster than P1.
9/15

<!-- Slide number: 10 -->
§2  Asymptotic Notation
10/15

<!-- Slide number: 11 -->
§2  Asymptotic Notation

![](Picture3.jpg)
2n
n2

n log n
f
n
Log n
n

11/15

<!-- Slide number: 12 -->
§2  Asymptotic Notation
s = microsecond = 10-6 seconds
ms = millisecond = 10-3 seconds
sec = seconds
min = minutes            yr = years
hr = hours
d = days
n
12/15

<!-- Slide number: 13 -->
§2  Asymptotic Notation
〖Example〗 Matrix addition

void  add ( int  a[ ][ MAX_SIZE ],
                   int  b[ ][ MAX_SIZE ],
                   int  c[ ][ MAX_SIZE ],
                   int  rows,  int  cols )
{
    int  i,  j ;
    for ( i = 0; i < rows; i++ )
          for ( j = 0; j < cols; j++ )
                c[ i ][ j ] = a[ i ][ j ] + b[ i ][ j ];
}
/*  (rows) */
/*  (rows  cols ) */
/*  (rows  cols ) */
T(rows, cols ) =  (rows  cols )
13/15

<!-- Slide number: 14 -->
§2  Asymptotic Notation

![](Picture5.jpg)
 General Rules
 FOR LOOPS: The running time of a for loop is at most the running time of the statements inside the for loop (including tests) times the number of iterations.
 NESTED FOR LOOPS: The total running time of a statement inside a group of nested loops is the running time of the statements multiplied by the product of the sizes of all the for loops.
 CONSECUTIVE STATEMENTS: These just add (which means that the maximum is the one that counts).
 IF / ELSE: For the fragment
		if ( Condition )  S1;
		else  S2;
	the running time is never more than the running time of the test plus the larger of the running time of S1 and S2.
14/15

<!-- Slide number: 15 -->
§2  Asymptotic Notation
 RECURSIONS:
〖Example〗 Fibonacci number:
Fib(0) = Fib(1) = 1,  Fib(n) = Fib(n1) + Fib(n2)
long int  Fib ( int  N )
{
	if  ( N <= 1 )
	    return  1;
	else
	    return  Fib( N  1 ) + Fib( N  2 );
}
/* T ( N ) */
Q: Why is it
so bad?
/* O( 1 ) */
/* O( 1 ) */
/*O(1)*/
/*T(N 1)*/
/*T(N 2)*/
T(N) = T(N 1) + T(N 2) + 2
  Fib(N)
Proof by induction
T(N) grows exponentially

15/15