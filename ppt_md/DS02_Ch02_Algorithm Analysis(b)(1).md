<!-- Slide number: 1 -->
§3   Compare the Algorithms
〖Example〗 Given (possibly negative) integers A1, A2, …, AN, find the maximum value of
Algorithm 1

Max sum is 0 if all the integers are negative.
int  MaxSubsequenceSum ( const int A[ ],  int  N )
{
	int  ThisSum,  MaxSum,  i,  j,  k;
/* 1*/ 	MaxSum = 0;   /* initialize the maximum sum */
/* 2*/ 	for( i = 0; i < N; i++ )  /* start from A[ i ] */
/* 3*/ 	      for( j = i; j < N; j++ ) {   /* end at A[ j ] */
/* 4*/ 		ThisSum = 0;
/* 5*/ 		for( k = i; k <= j; k++ )
/* 6*/ 		      ThisSum += A[ k ];  /* sum from A[ i ] to A[ j ] */
/* 7*/ 		if ( ThisSum > MaxSum )
/* 8*/ 		      MaxSum = ThisSum;  /* update max sum */
	      }  /* end for-j and for-i */
/* 9*/ 	return  MaxSum;
}
Detailed analysis is given on p.18-19.

T( N ) = O( N3 )
1/8

<!-- Slide number: 2 -->
§3  Compare the Algorithms
Algorithm 2
int  MaxSubsequenceSum ( const int A[ ],  int  N )
{
	int  ThisSum,  MaxSum,  i,  j;
/* 1*/ 	MaxSum = 0;   /* initialize the maximum sum */
/* 2*/ 	for( i = 0; i < N; i++ )  {   /* start from A[ i ] */
/* 3*/ 	      ThisSum = 0;
/* 4*/ 	      for( j = i; j < N; j++ ) {   /* end at A[ j ] */
/* 5*/ 		ThisSum += A[ j ];  /* sum from A[ i ] to A[ j ] */
/* 6*/ 		if ( ThisSum > MaxSum )
/* 7*/ 		      MaxSum = ThisSum;  /* update max sum */
	      }  /* end for-j */
	}  /* end for-i */
/* 8*/ 	return  MaxSum;
}
T( N ) = O( N2 )
2/8

<!-- Slide number: 3 -->
§3  Compare the Algorithms
Algorithm 3
Divide and Conquer

conquer
divide
4

3
5
2
1
2
6
2

4
5
2
6

6

8

11

T ( N/2 )
O( N )
T ( N/2 )
The program can be found on p.21.
T ( N ) = 2 T( N/2 ) + c N ,      T(1) = O(1)
Also true for N  2k
= 2 [2 T( N/22 ) + c N/2] + c N
= 2k O(1) + c k N       where  N/2k = 1
= O( N log N )
3/8

<!-- Slide number: 4 -->
§3  Compare the Algorithms
Algorithm 4
On-line Algorithm
int MaxSubsequenceSum( const int  A[ ],  int  N )
{
	int  ThisSum, MaxSum, j;
/* 1*/ 	ThisSum = MaxSum = 0;
/* 2*/ 	for ( j = 0; j < N; j++ ) {
/* 3*/ 	      ThisSum += A[ j ];
/* 4*/ 	      if  ( ThisSum > MaxSum )
/* 5*/ 		MaxSum = ThisSum;
/* 6*/ 	      else if ( ThisSum < 0 )
/* 7*/ 		ThisSum = 0;
	}  /* end for-j */
/* 8*/ 	return MaxSum;
}
1

3
2
4
6
1
6
1

1

3     2     4     6

At any point in time, the algorithm can correctly give an answer to the subsequence problem for the data it has already read.
T( N ) = O( N )
A[ ] is scanned once only.
4/8

<!-- Slide number: 5 -->
§3  Compare the Algorithms
Running times of several algorithms for maximum subsequence sum (in seconds)

Algorithm

1

2

3

4

Time

O( N3 )
O( N2 )
O(N log N)
O( N )
Input Size

N =10
N =100
N =1,000
N =10,000
N =100,000

    0.00103
    0.47015
448.77
     NA
     NA
    0.00045
    0.01112
    1.1233
111.13
     NA
  0.00066
  0.00486
  0.05843
  0.68631
  8.0113
  0.00034
  0.00063
  0.00333
  0.03042
  0.29832

Note: The time required to read the input is not included.
5/8

<!-- Slide number: 6 -->
§4   Logarithms in the Running Time
〖Example〗 Binary Search:
    Given:    A [0]   A [1]  ……   A [N  1] ;  X
     Task:      Find  X
     Output:   i      if  X = =  A [ i ]
                    1    if  X  is not found
low
mid
high

X ~  A [mid]
<
==
>

low
high = mid  1

low= mid + 1
high

mid
6/8

<!-- Slide number: 7 -->
§4  Logarithms in the Running Time
int BinarySearch ( const ElementType  A[ ],
			    ElementType  X,  int  N )
{
	int  Low, Mid, High;
/* 1*/ 	Low = 0;  High = N - 1;
/* 2*/ 	while ( Low <= High ) {
/* 3*/ 	      Mid = ( Low + High ) / 2;
/* 4*/ 	      if ( A[ Mid ] < X )
/* 5*/ 		Low = Mid + 1;
	      else
/* 6*/ 		if ( A[ Mid ] > X )
/* 7*/ 		      High = Mid - 1;
		else
/* 8*/ 		      return  Mid; /* Found */
	}  /* end while */
/* 9*/ 	return  NotFound; /* NotFound is defined as -1 */
}
T(N) = ?
Very useful in case the data are static and is in sorted order (e.g. find words from a dictionary).
Home work:
Self-study Euclid’s Algorithm
and Exponentiation
Tworst( N ) = O( log N )
7/8

<!-- Slide number: 8 -->
§5   Checking Your Analysis
When T(N) = O(N), check if T(2N)/T(N)  2
When T(N) = O(N2), check if T(2N)/T(N)  4
When T(N) = O(N3), check if T(2N)/T(N)  8
… …

Method  1

Method  2
When T(N) = O( f (N) ), check if
Read the example given on p.28 (Figures 2.12 & 2.13).
8/8

<!-- Slide number: 9 -->
Laboratory Project 1

Performance Measurement
Normal: Search
Hard: A+B
Due:  Tuesday, March 17th, 2026 at 10:00pm
                  Real Programmers
    don't comment their code.
   If it was hard to write,
it should be hard to understand
and harder to modify.
I will not read and grade
any program which has
less than 30% lines
commented.

![family2_face](Picture10.jpg)