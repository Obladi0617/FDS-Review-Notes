<!-- Slide number: 1 -->
§3  The Stack ADT
6
5

1.  ADT

6

      A stack is a Last-In-First-Out (LIFO) list, that is, an ordered list in which insertions and deletions are made at the top only.

5
4
Objects:  A finite ordered list with zero or more elements.
3
5
2
Operations:
 Int  IsEmpty( Stack S );
 Stack CreateStack( );
 DisposeStack( Stack S );
 MakeEmpty( Stack S );
 Push( ElementType X, Stack S );
 ElementType  Top( Stack S );
 Pop( Stack S );
6
1
Note: A Pop (or Top) on an empty stack is an error in the stack ADT.
      Push on a full stack is an implementation error but not an ADT error.

1/12

<!-- Slide number: 2 -->
§3  The Stack ADT
2.  Implementations
 Linked List Implementation (with a header node)
  TmpCell->Next = S->Next
 Push:

  S->Next = TmpCell
Element

 Top:
return S->Next->Element

Element


TmpCell

S


FirstCell

 Pop:

 FirstCell = S->Next
Element


Element


Element
NULL

S


S

 S->Next = S->Next->Next
 free ( FirstCell )
          Easy!  Simply keep
another stack as
a recycle bin.

    But, the calls to
    malloc and free
are expensive.
2/12

<!-- Slide number: 3 -->
§3  The Stack ADT
 Array Implementation
struct  StackRecord {
	int     Capacity ;              /* size of stack */
	int     TopOfStack;          /* the top pointer */
	/* ++ for push, -- for pop, -1 for empty stack */
	ElementType  *Array;    /* array for stack elements */
 } ;
Note:  The stack model must be well encapsulated.  That is, no part of your code, except for the stack routines, can attempt to access the Array or TopOfStack variable.
           Error check must be done before Push or Pop (Top).
Read Figures 3.38-3.52 for detailed implementations of stack operations.
3/12

<!-- Slide number: 4 -->
§3  The Stack ADT
3.  Applications
 Balancing Symbols

![DARTS](Picture6.jpg)
Check if parenthesis ( ), brackets [ ], and braces { } are balanced.
Algorithm  {
    Make an empty stack S;
    while (read in a character c) {
        if (c is an opening symbol)
            Push(c, S);
        else if (c is a closing symbol) {
            if (S is empty)  { ERROR; exit; }
            else  {  /* stack is okay */
                if  (Top(S) doesn’t match c)  { ERROR, exit; }
                else  Pop(S);
            }  /* end else-stack is okay */
        }  /* end else-if-closing symbol */
    } /* end while-loop */
    if (S is not empty)  ERROR;
}
T( N ) = O ( N )
where N is the length
of the expression.
This is an
on-line algorithm.
4/12

<!-- Slide number: 5 -->
§3  The Stack ADT
 Postfix Evaluation
〖Example〗An infix expression:       a  b  c  d  e
                       A prefix expression:      a  b c  d e
                       A postfix expression:   a b c   d e  
operator with
the highest precedence
Reverse Polish notation
operator
operand
〖Example〗 6 2  3  4 2    =  ?
8
Get token: 6 ( operand )
Get token: 2 ( operand )

Get token:  ( operator )
Get token: 3 ( operand )

2
top

Get token:  ( operator )
Get token: 4 ( operand )

2
3
4
8
top

top

top

top

top

Get token: 2 ( operand )
Get token:  ( operator )

6

2
= 3
6

3

0

8

top

top

top

top

top

top

top

top

Get token:  ( operator )
3

3
    Pop:  8

= 0
top

top

top

= 8
top


top

4


2
= 8
0
8
T( N ) = O ( N ).  No need to know precedence rules.
5/12

<!-- Slide number: 6 -->
§3  The Stack ADT
 Infix to Postfix Conversion
〖Example〗  a  b  c  d  =  ?
 a b c   d 
Note:
  The order of operands is the same in infix and postfix.
  Operators with higher precedence appear before those with lower precedence.
Isn’t that
simple?

    Wait till
you see the next
example...
Output:
a
b
c


d

Get token: a (operand)
 Get token:  (plus)

Get token: b (operand)
 Get token:  (times)

Get token: c (operand)
 Get token:  (minus)
   ?


top

Get token: d (operand)
   ?
   ?




top

top

top

top

top

top

6/12

<!-- Slide number: 7 -->
§3  The Stack ADT
〖Example〗  a  ( b  c )  d  =  ?
 a b c   d 

Output:
a
b
c


d

 Get token: a (operand)
 Get token:  (times)

 Get token: ( (lparen)
 Get token: b (operand)

+
top

 Get token:  (plus)
 Get token: c (operand)
  ( ?

(
top

top

 Get token: ) (rparen)
 Get token:  (divide)

(   ?




top

top

top

 Get token: d (operand)
   ?

top

top

top

NO?!
T( N ) = O ( N )
7/12

<!-- Slide number: 8 -->
§3  The Stack ADT
Solutions:
 Never pop a ( from the stack except when processing a ) .
 Observe that when (  is not in the stack, its precedence is the highest; but when it is in the stack, its precedence is the lowest.  Define in-stack precedence and incoming precedence for symbols, and each time use the corresponding precedence for comparison.
Note:  a – b – c will be converted to a b – c –.  However, 2^2^3 (        ) must be converted to 2 2 3 ^ ^, not 2 2 ^ 3 ^ since exponentiation associates right to left.
8/12

<!-- Slide number: 9 -->
§3  The Stack ADT
 Function Calls
-- System Stack
Recursion can always be completely removed.
Non recursive programs are generally faster than
equivalent recursive programs.
However, recursive programs are in general
much simpler and easier to understand.

f p

         Well, if 1 million elements
are not enough to crash
your program,
try a larger one.
Old  Frame  Pointer
s p

          What will happen
      if L contains 1 million
elements?
Return  Address
s p

        What’s wrong
with it?
Local Variables

s p

tail recursion
f p

f p

Stack  Frame
s p

s p

Return  Address
void  PrintList ( List L )
{
    if ( L != NULL )  {
        PrintElement ( L->Element );
        PrintList( L->next );
    }
}  /* a bad use of recursion */
void  PrintList ( List L )
{
top:  if ( L != NULL )  {
           PrintElement ( L->Element );
           L = L->next;
           goto top; /* do NOT do this */
         }
}  /* compiler removes recursion */

9/12

<!-- Slide number: 10 -->
§4  The Queue ADT

1.  ADT
4
A queue is a First-In-First-Out (FIFO) list, that is, an ordered list in which insertions take place at one end and deletions take place at the opposite end.
3
2

Objects:  A finite ordered list with zero or more elements.
1

Operations:
 int  IsEmpty( Queue Q );
 Queue CreateQueue( );
 DisposeQueue( Queue Q );
 MakeEmpty( Queue Q );
 Enqueue( ElementType X, Queue Q );
 ElementType  Front( Queue Q );
 Dequeue( Queue Q );
2
1
2

1

10/12

<!-- Slide number: 11 -->
§4  The Queue ADT
2.  Array Implementation of Queues
     (Linked list implementation is trivial)
struct  QueueRecord {
	int     Capacity ;   /* max size of queue */
	int     Front;          /* the front pointer */
	int     Rear;           /* the rear pointer */
	int     Size;  /* Optional - the current size of queue */
	ElementType  *Array;    /* array for queue elements */
 } ;
〖Example〗  Job Scheduling in an Operating System
0
1
2
3
4
5
6

Job 1

Job 2

Job 3
Job 4
Job 5
Job 6
Job 7

Rear

Rear

Front

Rear

Rear

Rear

Rear
Front
Rear
Front
Rear
Enqueue Job 1
Enqueue Job 2
Enqueue Job 3
Dequeue Job 1
Enqueue Job 4
Enqueue Job 5
Enqueue Job 6
Dequeue Job 2
Enqueue Job 7
Enqueue Job 8
11/12

<!-- Slide number: 12 -->
§4  The Queue ADT
Circular Queue:
[ 0 ]
[ 5 ]

[ 4 ]
[ 1 ]

[ 3 ]
[ 2 ]
Rear
Question:
Why is the queue
announced full
while there is
still a free
space  left?

Rear

Do you have
a better idea?
Enqueue Job 1
Rear
Front
Rear
Front

Job
5

Job
6
Are you kidding?
Of course I do!
Enqueue Job 2

Enqueue Job 3
Job
4
Job
1

Dequeue Job 1

Enqueue Job 4
Rear

Job
2
Job
3
Enqueue Job 5
Rear

The queue
is full
Enqueue Job 6
Front
Enqueue Job 7
Rear

Note: Adding a Size field can avoid wasting one empty space to distinguish “full” from “empty”.  Do you have any other ideas?
12/12

<!-- Slide number: 13 -->
Bonus Problem 1

LRU-K
(2 points)
Due:  Tuesday, June 16th, 2026 at 10:00pm
The problem can be found and submitted at
 https://pintia.cn/