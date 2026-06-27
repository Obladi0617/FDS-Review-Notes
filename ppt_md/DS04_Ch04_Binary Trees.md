<!-- Slide number: 1 -->
CHAPTER  4
TREES
§1  Preliminaries
1.  Terminology

![family1_face](Picture22.jpg)

![family1_face](Picture24.jpg)

![family2_face](Picture23.jpg)

![family5_face](Picture25.jpg)

![family8_face](Picture31.jpg)

![family6_face](Picture26.jpg)

![family3_face](Picture29.jpg)

![family4_face](Picture30.jpg)

![family8_face](Picture32.jpg)

![family7_face](Picture28.jpg)

![family6_face](Picture27.jpg)

![family5_face](Picture49.jpg)

![family4_face](Picture50.jpg)

![family8_face](Picture51.jpg)

![family4_face](Picture53.jpg)

![family1_face](Picture52.jpg)

![family7_face](Picture54.jpg)

![family2_face](Picture55.jpg)
Pedigree Tree
( binary tree )
Lineal Tree
1/16

<!-- Slide number: 2 -->
§1  Preliminaries
【Definition】A tree is a collection of nodes.  The collection can be empty; otherwise, a tree consists of
  (1)  a distinguished node r, called the root;
  (2)  and zero or more nonempty (sub)trees T1, , Tk, each of whose roots are connected by a directed edge from r.
Note:
  Subtrees must not connect together.  Therefore every node in the tree is the root of some subtree.
  There are              edges in a tree with N nodes.
  Normally the root is drawn at the top.
N  1
2/16

<!-- Slide number: 3 -->
§1  Preliminaries
  degree of a node ::= number of subtrees of the node.  For example, degree(A) = 3, degree(F) = 0.
A

B
C
D

E
F
G
H
I
J

K
L
M
  degree of a tree ::=
      For example, degree of this tree = 3.
  parent ::= a node that has subtrees.
  children ::= the roots of the subtrees of a parent.
  siblings ::= children of the same parent.
  leaf ( terminal node ) ::= a node with degree 0 (no children).
3/16

<!-- Slide number: 4 -->
§1  Preliminaries
  path from n1 to nk ::= a (unique) sequence of nodes n1, n2, …, nk  such that ni is the parent of ni+1 for 1  i < k.
A

B
C
D

E
F
G
H
I
J

K
L
M
  length of path ::= number of edges on the path.
  depth of ni ::= length of the unique path from the root to ni.   Depth(root) = 0.
  height of ni ::= length of the longest path from ni to a leaf.  Height(leaf) = 0, and height(D) = 2.
  height (depth) of a tree ::= height(root) = depth(deepest leaf).
  ancestors of a node ::= all the nodes along the path from the node up to the root.
  descendants of a node ::= all the nodes in its subtrees.
4/16

<!-- Slide number: 5 -->
§1  Preliminaries
2.  Implementation
  List Representation
( A )
A

B
C
D

E
F
G
H
I
J

K
L
M
So the size of each node
 depends on the number of
branches.
Hmmm... That’s not good.
( A ( B, C, D ) )
( A ( B ( E, F ), C ( G ), D ( H, I, J ) ) )
( A ( B ( E ( K, L ), F ), C ( G ), D ( H ( M ), I, J ) ) )
K
E

B

L

F
A

C

G

H

M

D

I

J
5/16

<!-- Slide number: 6 -->
§1  Preliminaries
  FirstChild-NextSibling Representation
Element
FirstChild
NextSibling

A

N

B

C

D

N

E

F
N
N
G
N
N
H

I
N

J
N
N

K
N

L
N
N
M
N
N

A

B
C
D

E
F
G
H
I
J

K
L
M
Note:  The representation is not unique since the children in a tree can be of any order.
6/16

<!-- Slide number: 7 -->
§2  Binary Trees
【Definition】A binary tree is a tree in which no node can have more than two children.
Rotate the FirstChild-NextSibling tree clockwise by 45.
A

N

B

C

D

N

E

F
N
N
G
N
N
H

I
N

J
N
N

K
N

L
N
N
M
N
N

45

A

N

B

C

D

N

E

F
N
N
G
N
N
H

I
N

J
N
N

K
N

L
N
N
M
N
N

Right
Left

Element
Left
Right

7/16

<!-- Slide number: 8 -->
§2  Binary Trees
  Expression Trees (syntax trees)
+

A



D

B
C

〖Example〗  Given an infix expression:
                         A + B  C  D
 Constructing an Expression Tree
     (from postfix expression)
〖Example〗  ( a + b ) * ( c * ( d + e ) ) =
a b + c d e + * *

+

a
b

a

+

*

b

c

d

e

c

*

+

T2

a
T2
+
*
T1

a
b
c
+

d
e
b
T1

c
+
T1

d
e
T2
d
e

T1
T2

8/16

<!-- Slide number: 9 -->
§2  Binary Trees
 Tree Traversals —— visit each node exactly once
  Preorder Traversal
  Postorder Traversal
void  preorder ( tree_ptr  tree )
{  if  ( tree )   {
        visit ( tree );
        for (each child C of tree )
            preorder ( C );
    }
}
void  postorder ( tree_ptr  tree )
{  if  ( tree )   {
        for (each child C of tree )
            postorder ( C );
        visit ( tree );
    }
}
  Levelorder Traversal
void  levelorder ( tree_ptr  tree )
{   enqueue ( tree );
    while (queue is not empty) {
        visit ( T = dequeue ( ) );
        for (each child C of T )
            enqueue ( C );
    }
}
1

2

4
5
3

6
7
1
2
3
4
5
6
7

1

2

3

4

5

6

7
9/16

<!-- Slide number: 10 -->
§2  Binary Trees
  Inorder Traversal
Iterative Program
void  iter_inorder ( tree_ptr  tree )
{ Stack  S = CreateStack( MAX_SIZE );
  for ( ; ; )  {
     for ( ; tree; tree = tree->Left )
        Push ( tree, S ) ;
     tree = Top ( S );  Pop( S );
     if ( ! tree )  break;
     visit ( tree->Element );
     tree = tree->Right;   }
}
void  inorder ( tree_ptr  tree )
{  if  ( tree )   {
        inorder ( tree->Left );
        visit ( tree->Element );
        inorder ( tree->Right );
   }
}
〖Example〗  Given an
    infix expression:
             A + B  C  D
+

A



D

B
C

Then inorder traversal    A + B  C  D
      postorder traversal    A B C  D  +
       preorder traversal    + A   B C D
10/16

<!-- Slide number: 11 -->
§2  Binary Trees
〖Example〗 Directory listing in a hierarchical file system.
/usr

mark
alex
bill

book
course
hw.c
hw.c
work
course

ch1.c
ch2.c
ch3.c
cop3530
cop3212

fall96
spr97
sum97
fall96
fall97

syl.r
syl.r
syl.r
grades
p1.r
p2.r
p2.r
p1.r
grades
Unix directory
Listing format:  files that are of depth di will have their names indented by di tabs.
11/16

<!-- Slide number: 12 -->
§2  Binary Trees
/usr
    mark
            book
	Ch1.c
	Ch2.c
	Ch3.c
            course
	cop3530
	          fall96
		syl.r
	          spr97
		syl.r
	          sum97
		syl.r
            hw.c
    alex
            hw.c
    bill
            work
            course
	cop3212
	          fall96
		grades
		p1.r
		p2.r
	          fall97
		p2.r
		p1.r
		grades
static void  ListDir ( DirOrFile D, int Depth )
{
    if  ( D is a legitimate entry )   {
        PrintName (D, Depth );
        if ( D is a directory )
            for (each child C of D )
                ListDir ( C, Depth + 1 );
    }
}
T ( N ) = O( N )
Note: Depth is an internal variable and must not be seen by the user of this routine.  One solution is to define another interface function as the following:
void ListDirectory ( DirOrFile  D )
{	ListDir( D, 0 );                 }
12/16

<!-- Slide number: 13 -->
§2  Binary Trees
〖Example〗 Calculating the size of a directory.
/usr
1

mark
alex
bill
1
1
1

book
course
hw.c
hw.c
work
course
1
1
6
8
1
1

ch1.c
ch2.c
ch3.c
cop3530
cop3212
3
2
4
1
1

fall96
spr97
sum97
fall96
fall97
1
1
1
1
1

syl.r
syl.r
syl.r
grades
p1.r
p2.r
p2.r
p1.r
grades
1
5
2
3
4
1
2
7
9
Unix directory with file sizes
static int  SizeDir ( DirOrFile D )
{
    int TotalSize;
    TotalSize = 0;
    if  ( D is a legitimate entry )   {
        TotalSize = FileSize( D );
        if ( D is a directory )
            for (each child C of D )
                TotalSize += SizeDir(C);
    } /* end if D is legal */
    return TotalSize;
}
T ( N ) = O( N )
13/16

<!-- Slide number: 14 -->
§2  Binary Trees
  Threaded Binary Trees
                Here comes
       the typical question of mine:
     Why do we need
      threaded binary trees?
Because I enjoy giving
you headaches ... Just kidding.
Okay, think of a full
binary tree with n nodes.
How many links are there?
Any clue on how to
improve the situation?
We can replace
the null links by “threads”
which will make traversals
easier.
    Then who should
take the credit?
They are
A. J. Perlis and C. Thornton.
    You are such a
genius !
n + 1.
Oh well,
I wish I’d have really done it
Of course not!
How many of them
are NULL?
You got it!
Can I stand that?

14/16

<!-- Slide number: 15 -->
§2  Binary Trees
Rule 1:  If Tree->Left is null, replace it with a pointer to the inorder predecessor of Tree.
Rule 2:  If Tree->Right is null, replace it with a pointer to the inorder successor of Tree.
Rule 3:  There must not be any loose threads.  Therefore a threaded binary tree must have a head node of which the left child points to the first node.

typedef  struct  ThreadedTreeNode  *PtrTo  ThreadedNode;
typedef  struct  PtrToThreadedNode  ThreadedTree;
typedef  struct  ThreadedTreeNode {
       int           		LeftThread;   /* if it is TRUE, then Left */
       ThreadedTree  	Left;      /* is a thread, not a child ptr.   */
       ElementType	Element;
       int           		RightThread; /* if it is TRUE, then Right */
       ThreadedTree  	Right;    /* is a thread, not a child ptr.   */
}
15/16

<!-- Slide number: 16 -->
§2  Binary Trees
〖Example〗  Given the syntax tree of an expression (infix)
A + B  C  D
head node

F

F

F

+

F

T

A

T
F



F

F



F
T

D

T

T

B

T
T

C

T
+

A



D

B
C

16/16