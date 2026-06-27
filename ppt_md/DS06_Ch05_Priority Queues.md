<!-- Slide number: 1 -->
CHAPTER  5
PRIORITY  QUEUES  (HEAPS)
—— delete the element with the highest \ lowest priority
§1  ADT Model
Objects:  A finite ordered list with zero or more elements.
Operations:
 PriorityQueue  Initialize( int MaxElements );
 void  Insert( ElementType X, PriorityQueue H );
 ElementType  DeleteMin( PriorityQueue H );
 ElementType  FindMin( PriorityQueue H );

1/15

<!-- Slide number: 2 -->
§2  Simple Implementations
  Array :
Insertion — add one item at the end  ~   ( 1 )
Deletion — find the largest \ smallest key  ~   ( n )
                    remove the item and shift array ~  O( n )
  Linked List :
Insertion — add to the front of the chain  ~   ( 1 )
Deletion — find the largest \ smallest key  ~   ( n )
                    remove the item  ~ ( 1 )
  Ordered Array :
Insertion — find the proper position  ~  O( n )
                     shift array and add the item  ~  O( n )
Deletion — remove the first \ last item  ~ ( 1 )
Better since there are never more deletions than insertions
  Ordered Linked List :
Insertion — find the proper position  ~  O( n )
                     add the item  ~ ( 1 )
Deletion — remove the first \ last item  ~ ( 1 )
2/15

<!-- Slide number: 3 -->
§2  Simple Implementations
  Binary Search Tree :
There are many operations
related to AVL tree that we don’t really
need for a priority queue.
Besides, pointers are
always dangerous.
           Ah!  That’s a good idea!
          Both insertion and deletion will take
O(log N) only.
           Oh, right, then we must always
delete from the left subtrees….
But hey, what if we keep
a balanced tree?
         I bet you have a better option?
Hey you are getting smarter!
Yes a balanced tree such as AVL tree
is not a bad idea since only a
constant factor will be added to
the run time.  However…
Now you begin to know me  
           Oh no… what’s wrong?
Well, insertions are random,
but deletions are NOT.
We are supposed to delete
The minimum element only.

3/15

<!-- Slide number: 4 -->
§3  Binary Heap
1. Structure Property:
【Definition】A binary tree with n nodes and height h is complete  iff  its nodes correspond to the nodes numbered from 1 to n in the perfect binary tree of height h.

A complete binary tree of height  h  has between
and
nodes.
2h
2h+1  1
h =  log N 

1

2

3

4

8
9
5

10
11
6

12
13
7

14
15
  Array Representation :  BT [ n + 1 ]  ( BT [ 0 ] is not used)
A

B

C

D

H
I
E
F
G

J
BT
0
1
2
3
4
5
6

A
B
C
D
E
F
7
8
9
10
11
12
13
G
H
I
J

4/15

<!-- Slide number: 5 -->
§3  Binary Heap
【Lemma】If a complete binary tree with n nodes is represented sequentially, then for any node with index i,  1  i  n, we have:
5/15

<!-- Slide number: 6 -->
§3  Binary Heap
PriorityQueue  Initialize( int  MaxElements )
{
     PriorityQueue  H;
     if ( MaxElements < MinPQSize )
	return  Error( "Priority queue size is too small" );
     H = malloc( sizeof ( struct HeapStruct ) );
     if ( H ==NULL )
	return  FatalError( "Out of space!!!" );
     /* Allocate the array plus one extra for sentinel */
     H->Elements = malloc(( MaxElements + 1 ) * sizeof( ElementType ));
     if ( H->Elements == NULL )
	return  FatalError( "Out of space!!!" );
     H->Capacity = MaxElements;
     H->Size = 0;
     H->Elements[ 0 ] = MinData;  /* set the sentinel */
     return  H;
}
6/15

<!-- Slide number: 7 -->
§3  Binary Heap
2. Heap Order Property:
【Definition】A min tree is a tree in which the key value in each node is no larger than the key values in its children (if any).  A min heap is a complete binary tree that is also a min tree.
Note: Analogously, we can declare a max heap by changing the heap order property.
The largest key

The smallest key

9
[1]

[2]
6
[3]
3

5
[4]
10
[1]

[2]
20
[3]
83

50
[4]
A max heap
A min heap
7/15

<!-- Slide number: 8 -->
§3  Binary Heap
3. Basic Heap Operations:
  insertion
 Sketch of the idea:
The only possible position
for a new node
since a heap must be
a complete binary tree.
10
[1]

[2]
12
[3]
20

15
18

[4]
[5]
[6]
9
17
9
10
21
17
20
Case 1 :  new_item = 21
20
<
21
Case 2 :  new_item = 17
20
>
17
10
<
17
Case 3 :  new_item = 9
20
>
9
10
>
9
8/15

<!-- Slide number: 9 -->
§3  Binary Heap
/* H->Element[ 0 ] is a sentinel */
void  Insert( ElementType  X,  PriorityQueue  H )
{
     int  i;

     if ( IsFull( H ) ) {
	Error( "Priority queue is full" );
	return;
     }

     for ( i = ++H->Size; H->Elements[ i / 2 ] > X; i /= 2 )
	H->Elements[ i ] = H->Elements[ i / 2 ];

     H->Elements[ i ] = X;
}
H->Element[ 0 ] is a sentinel that is no larger than the minimum element in the heap.
Percolate up
Faster than swap
T (N) = O ( log N )
9/15

<!-- Slide number: 10 -->
§3  Binary Heap
  DeleteMin
Ah!  That’s simple --
we only have to delete
the root node ...
 Sketch of the idea:
And re-arrange
the rest of the tree so that
it’s still a min heap.
The node which must be
removed to keep a
complete binary tree.
  move 18 up to the root
10
[1]

[2]
12
[3]
20

15
18
[4]
[5]

18
12
15

18

<
12
18
  find the smaller child of 18

<
15
18
18

T (N) = O ( log N )
10/15

<!-- Slide number: 11 -->
§3  Binary Heap
ElementType  DeleteMin( PriorityQueue  H )
{
    int  i, Child;
    ElementType  MinElement, LastElement;
    if ( IsEmpty( H ) ) {
         Error( "Priority queue is empty" );
         return  H->Elements[ 0 ];   }
    MinElement = H->Elements[ 1 ];  /* save the min element */
    LastElement = H->Elements[ H->Size-- ];  /* take last and reset size */
    for ( i = 1; i * 2 <= H->Size; i = Child ) {  /* Find smaller child */
         Child = i * 2;
         if (Child != H->Size && H->Elements[Child+1] < H->Elements[Child])
	       Child++;
         if ( LastElement > H->Elements[ Child ] )   /* Percolate one level */
	       H->Elements[ i ] = H->Elements[ Child ];
         else     break;   /* find the proper position */
    }
    H->Elements[ i ] = LastElement;
    return  MinElement;
}
Can we remove it by adding another sentinel?
What if this condition is omitted?
Percolate down
11/15

<!-- Slide number: 12 -->
§3  Binary Heap
4. Other Heap Operations:
Note: Finding any key except the minimum one will have to take a linear scan through the entire heap.
  DecreaseKey ( P, , H )
Percolate up
sys. admin.
Lower the value of the key in the heap H at position P by a positive amount of ……so my programs can run with highest priority .
  IncreaseKey ( P, , H )
Percolate down
Increases the value of the key in the heap H at position P by a positive amount of ……drop the priority of a process that is consuming excessive CPU time.
sys. admin.
12/15

<!-- Slide number: 13 -->
§3  Binary Heap
  Delete ( P, H )
DecreaseKey(P, , H); DeleteMin(H)
sys. admin.
Remove the node at position P from the heap H  …… delete the process that is terminated (abnormally) by a user.
              Nehhhhh that would be
toooo slow !
  BuildHeap ( H )
N  successive Insertions ?
sys. admin.
Place N input keys into an empty heap H.
150, 80, 40, 30, 10, 70, 110, 100, 20, 90, 60, 50, 120, 140, 130
PercolateDown (7)
150

80

40

30

100
20
10

90
60
70

50
120
110

140
130
10

150

PercolateDown (6)
PercolateDown (5)
T (N) = ?
20

150
10

80
PercolateDown (4)

20

30
30

150
60

80
50

70
PercolateDown (3)
PercolateDown (2)

PercolateDown (1)
13/15

<!-- Slide number: 14 -->
§3  Binary Heap
【Theorem】For the perfect binary tree of height h containing 2h+1  1 nodes, the sum of the heights of the nodes is 2h+1  1  (h + 1).
T ( N ) = O ( N )

§4  Applications of Priority Queues
〖Example〗Given a list of N elements and an integer k.  Find the kth largest element.
How many methods can you think of to solve this problem?  What are their complexities?
14/15

<!-- Slide number: 15 -->
§5  d-Heaps
---- All nodes have d children
1

2
3
5

4
7
10
13
15
6
8
17
9

11
9
3-heap
Question:  Shall we make d as large as possible?
Note:  DeleteMin will take d  1 comparisons to find the smallest child.   Hence the total time complexity would be O(d logd N).
           *2 or /2 is merely a bit shift, but *d or /d is not.
           When the priority queue is too large to fit entirely in main memory, a d-heap will become interesting.
15/15