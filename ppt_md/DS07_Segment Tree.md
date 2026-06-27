<!-- Slide number: 1 -->
The Segment Tree – motivation
Given an array A[1000000], and we need to frequently calculate the sum of the numbers in an arbitrary range [L, R].

L
R
ElementType  Query ( ElementType A[ ],  int L, int R )
{
      ElementType sum = 0;
      for  ( int i = L; i <= R; ++i )
          sum += A[i];
      return sum;
}
T( N ) = O ( N )
👎 as a frequent operation

<!-- Slide number: 2 -->

The Segment Tree – structure
25
[0,4]

14
[0,2]
11
[3,4]

8
[3]
3
[4]
9
[0,1]
5
[2]

7
[0]
2
[1]
int A[5];

7
2
5
8
3
[0]
[1]
[2]
[3]
[4]

<!-- Slide number: 3 -->
The Segment Tree – how to build?
25
[0,4]
stored value
[1]
not stored, but computed on the fly

14
[0,2]
11
[3,4]
[3]
[2]

8
[3]
3
[4]
9
[0,1]
5
[2]
[7]
[4]
[5]
[6]

7
[0]
2
[1]
A complete binary tree that can be
stored in an array: int tree[10];
[9]
[8]
int A[5];

S( N ) = O ( 2N–1 )
7
2
5
8
3
[0]
[1]
[2]
[3]
[4]

<!-- Slide number: 4 -->
The Segment Tree – how to build?
void Build ( int node, int start, int end )
{
    // Base Case: Leaf Node
    if ( start == end ) {
        tree[ node ] = A[ start ];
        return;
    }

    // Recursive Step: Split and Build Children
    int mid = ( start + end ) / 2;
    Build ( 2 * node, start, mid );
    Build ( 2 * node + 1, mid + 1, end );

    // Merge Logic: Sum of children
    tree[ node ] = tree[ 2 * node ] + tree[ 2 * node + 1 ];
}
T( N ) = O ( N )
but run only once

<!-- Slide number: 5 -->
The Segment Tree – query
Partial Overlap
25
[0,4]

Partial Overlap
Total Overlap
14
[0,2]
11
[3,4]

No Overlap
Total Overlap
Unvisited
Unvisited
8
[3]
3
[4]
9
[0,1]
5
[2]

Unvisited
Unvisited
7
[0]
2
[1]
[   L = 2            ,         R = 4 ]

7
2
5
8
3
[0]
[1]
[2]
[3]
[4]

<!-- Slide number: 6 -->
The Segment Tree – query
👍 T( N ) = O ( log N )
int Query ( int node, int start, int end, int L, int R )
{
    // Case 1: No Overlap (Node is completely outside query range)
    if ( R < start || end < L ) {
        return 0;
    }

    // Case 2: Total Overlap (Node is completely inside query range)
    if ( L <= start && end <= R ) {
        return tree[ node ];
    }

    // Case 3: Partial Overlap (We need to go deeper into both children)
    int mid = ( start + end ) / 2;
    int left_sum = Query ( 2 * node, start, mid, L, R );
    int right_sum = Query ( 2 * node + 1, mid + 1, end, L, R );

    return left_sum + right_sum;
}

<!-- Slide number: 7 -->
The Segment Tree – update
In the range
25
[0,4]

In the range
Unvisited
14
[0,2]
11
[3,4]

Unvisited
Found
Unvisited
Unvisited
8
[3]
3
[4]
9
[0,1]
5
[2]

Unvisited
Unvisited
7
[0]
2
[1]
A[ idx ] = 9

7
2
5
8
3
[0]
[1]
[2]
[3]
[4]

<!-- Slide number: 8 -->
The Segment Tree – update
Updated
26
[0,4]

Updated
Unvisited
14
[0,2]
12
[3,4]

Unvisited
Updated
Unvisited
Unvisited
9
[3]
3
[4]
9
[0,1]
5
[2]

Unvisited
Unvisited
7
[0]
2
[1]
A[ idx ] = 9

7
2
5
9
3
[0]
[1]
[2]
[3]
[4]

<!-- Slide number: 9 -->
The Segment Tree – update
👍 T( N ) = O ( log N )
void Update ( int node, int start, int end, int idx, int val )
{
    // Base Case: Leaf Node found
    if ( start == end ) {
        tree[ node ] = val;
        return;
    }

    // Recursive Step: Go left or right depending on where “idx” is
    int mid = (start + end) / 2;
    if ( start <= idx && idx <= mid ) {
        // Index is in the left child
        Update ( 2 * node, start, mid, idx, val );
    } else {
        // Index is in the right child
        Update ( 2 * node + 1, mid + 1, end, idx, val );
    }

    // Backtracking Step: Update current node based on new children values
    tree[ node ] = tree[ 2 * node ] + tree[ 2 * node + 1 ];
}

<!-- Slide number: 10 -->
The Segment Tree – notes
Not limited to sum, but applicable to any aggregation operator over a range, such as min, max, or average.
For more general RangeUpdate (e.g., add 10 to all numbers from index 2 to 1000), the lazy propagation strategy is effective (self study).