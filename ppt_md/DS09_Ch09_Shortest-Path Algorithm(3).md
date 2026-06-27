<!-- Slide number: 1 -->
§3  Shortest Path Algorithms
Given a digraph G = ( V, E ), and a cost function c( e ) for e  E( G ).   The length of a path P from source to destination is                  (also called weighted path length).
1.  Single-Source Shortest-Path Problem
Given as input a weighted graph, G = ( V, E ), and a distinguished vertex, s, find the shortest weighted path from s to every other vertex in G.
Negative-cost cycle
Note: If there is no negative-cost cycle, the shortest path from s to s is defined to be zero.
2
v1
v2

4
1
3
10

2
2
v3
v4
v5

8
4
6

5
1
v6
v7

2
v1
v2

4
1
–10

3
2
2
v3
v4
v5

8
4
6

5
1
v6
v7

1/11

<!-- Slide number: 2 -->
§3  Shortest Path Algorithms
  Unweighted Shortest Paths
 Sketch of the idea
0:    v3
1
2
v1
v2

v3
v4
v5

v6
v7

Breadth-first search
1:  
v1 and v6
2
0

3
2:  
v2 and v4
3:  
1
3
v5
and v7
 Implementation
Table[ i ].Dist ::= distance from s to vi  /* initialized to be  except for s */
Table[ i ].Known ::= 1 if vi is checked; or 0 if not
Table[ i ].Path ::= for tracking the path   /* initialized to be 0 */
2/11

<!-- Slide number: 3 -->
§3  Shortest Path Algorithms
void Unweighted( Table T )
{   int  CurrDist;
    Vertex  V, W;
    for ( CurrDist = 0; CurrDist < NumVertex; CurrDist ++ ) {
        for ( each vertex V )
	if ( !T[ V ].Known && T[ V ].Dist == CurrDist ) {
	    T[ V ].Known = true;
	    for ( each W adjacent to V )
	        if ( T[ W ].Dist == Infinity ) {
		T[ W ].Dist = CurrDist + 1;
		T[ W ].Path = V;
	        } /* end-if Dist == Infinity */
	} /* end-if !Known && Dist == CurrDist */
    }  /* end-for CurrDist */
}

If V is unknown yet has Dist < Infinity, then Dist is either CurrDist or CurrDist+1.
  T = O( |V|2 )
The worst case:
v8
v7
v6
v5
v3
v2
v1
v9
v4

3/11

<!-- Slide number: 4 -->
§3  Shortest Path Algorithms
 Improvement
1
2
void Unweighted( Table T )
{   /* T is initialized with the source vertex S given */
    Queue  Q;
    Vertex  V, W;
    Q = CreateQueue (NumVertex );  MakeEmpty( Q );
    Enqueue( S, Q ); /* Enqueue the source vertex */
    while ( !IsEmpty( Q ) ) {
        V = Dequeue( Q );
        T[ V ].Known = true; /* not really necessary */
        for ( each W adjacent to V )
	if ( T[ W ].Dist == Infinity ) {
	    T[ W ].Dist = T[ V ].Dist + 1;
	    T[ W ].Path = V;
	    Enqueue( W, Q );
	} /* end-if Dist == Infinity */
    } /* end-while */
    DisposeQueue( Q ); /* free memory */
}
v1
v2

v3
v4
v5

v6
v7

0
3
2

3
1
Dist Path
v1

0
v2

0
v3
0
0
v4

0
v5

0
v6

0
v7

0

1
v3
v7

2
v1
v5

v4

2
v1
v2

3
v2
1
v3
v6

3
v4
v3

v1

T = O( |V| + |E| )
4/11

<!-- Slide number: 5 -->
§3  Shortest Path Algorithms
  Dijkstra’s Algorithm (for weighted shortest paths)
Let S = { s and vi’s whose shortest paths have been found }
For any u  S,  define  distance [ u ] = minimal length of path { s  ( vi  S )  u }.  If the paths are generated in non-decreasing order, then
  the shortest path must go through ONLY vi  S ;
  u is chosen so that distance[ u ] = min{ wS | distance[ w ] }  (If u is not unique, then we may select any of them) ;  /* Greedy Method */
    Why?  If it is not true, then
there must be a vertex w on this path
that is not in S.  Then ...
  if distance [ u1 ] < distance [ u2 ] and we add u1 into S, then distance [ u2 ] may change.  If so, a shorter path from s to u2 must go through u1 and distance’ [ u2 ] = distance [ u1 ] + length(< u1, u2>).
5/11

<!-- Slide number: 6 -->
§3  Shortest Path Algorithms
void Dijkstra( Table T )
{   /* T is initialized by Figure 9.30 on p.303 */
    Vertex  V, W;
    for ( ; ; ) {
        V = smallest unknown distance vertex;
        if ( V == NotAVertex )
	break;
        T[ V ].Known = true;
        for ( each W adjacent to V )
	if ( !T[ W ].Known )
	    if ( T[ V ].Dist + Cvw < T[ W ].Dist ) {
	    	Decrease( T[ W ].Dist  to
			 T[ V ].Dist + Cvw );
		T[ W ].Path = V;
	    } /* end-if update W */
    } /* end-for( ; ; ) */
}
2
v1
v2

4
1
3
10

2
2
v3
v4
v5

8
4
6

5
1
v6
v7

/* O( |V| ) */

Dist Path
v1
0
0
v2

0
v3

0
v4

0
v5

0
v6

0
v7

0
2
v1
3
v4

1
v1
3
v4
9
v4
8
v3
6
v7
/* not work for edge with negative cost */
5
v4
Please read Figure 9.31 on p.304 for printing the path.
6/11

<!-- Slide number: 7 -->
§3  Shortest Path Algorithms
 Implementation 1
V = smallest unknown distance vertex;
/* simply scan the table – O( |V| ) */
Good if the graph is dense
T = O( |V|2 + |E| )
 Implementation 2
V = smallest unknown distance vertex;
/* keep distances in a priority queue and call DeleteMin – O( log|V| ) */
Decrease( T[ W ].Dist  to  T[ V ].Dist + Cvw );
Good if the graph is sparse
/* Method 1: DecreaseKey – O( log|V| ) */
T = O( |V| log|V| + |E| log|V| ) = O( |E| log|V| )
/* Method 2: insert W with updated Dist into the priority queue */
/* Must keep doing DeleteMin until an unknown vertex emerges */
T = O( |E| log|V| ) but requires |E| DeleteMin with |E| space
 Other improvements: Pairing heap (Ch.12) and Fibonacci heap (Ch. 11)
7/11

<!-- Slide number: 8 -->
§3  Shortest Path Algorithms
  Graphs with Negative Edge Costs
Hey I have a good idea:
           why don’t we simply add a constant
         to each edge and thus remove
negative edges?
Too simple, and naïve…
Try this one out:

2
1
2

– 2
1
3
4
2

void  WeightedNegative( Table T )
{   /* T is initialized by Figure 9.30 on p.303 */
    Queue  Q;
    Vertex  V, W;
    Q = CreateQueue (NumVertex );  MakeEmpty( Q );
    Enqueue( S, Q ); /* Enqueue the source vertex */
    while ( !IsEmpty( Q ) ) {
        V = Dequeue( Q );
        for ( each W adjacent to V )
	if ( T[ V ].Dist + Cvw < T[ W ].Dist ) {
	    T[ W ].Dist = T[ V ].Dist + Cvw;
	    T[ W ].Path = V;
	    if ( W is not already in Q )
	        Enqueue( W, Q );
	} /* end-if update */
    } /* end-while */
    DisposeQueue( Q ); /* free memory */
}
T = O( |V|  |E| )
/* each vertex can dequeue at most |V| times */
/* no longer once per edge */

/* negative-cost cycle will cause indefinite loop */
8/11

<!-- Slide number: 9 -->
§3  Shortest Path Algorithms
  Acyclic Graphs
If the graph is acyclic, vertices may be selected in topological order since when a vertex is selected, its distance can no longer be lowered without any incoming edges from unknown nodes.
T = O( |E| + |V| ) and no priority queue is needed.
 Application: AOE ( Activity On Edge ) Networks
                                                        ——  scheduling a project
Signals the completion of ai
ai ::= activity
vj

 Index of  vertex
EC Time

Lasting Time

Slack Time
LC Time
  EC[ j ] \ LC[ j ] ::= the earliest \ latest completion time for node vj
 CPM ( Critical Path Method )
9/11

<!-- Slide number: 10 -->
§3  Shortest Path Algorithms
〖Example〗  AOE network of a hypothetical project

1

6

0

start

4

8

finish

2

7

3

5

6
16
0
7
18
4
14
5
7
a0=6
a3=1
a6=9
a9=2
a1=4
a7=7
a10=4
a4=1
a2=5
a8=4
a5=2
6
16
0
7
18
6
14
5
7

2
2

a11=0
3
Dummy activity
  Calculation of EC:  Start from v0, for any ai = <v, w>, we have
  Calculation of LC:  Start from the last vertex v8, for any ai = <v, w>, we have
  Slack Time of <v,w> =
  Critical Path ::= path consisting entirely of zero-slack edges.
10/11

<!-- Slide number: 11 -->
§3  Shortest Path Algorithms
2.  All-Pairs Shortest Path Problem
For all pairs of vi and vj ( i  j ), find the shortest path between.
Method 1  Use  single-source algorithm  for |V| times.
T = O( |V|3 ) – works fast on sparse graph.
Method 2  O( |V|3 ) algorithm given in Ch.10, works faster on dense graphs.
11/11

<!-- Slide number: 12 -->
Laboratory Project 3

Normal: Dijkstra Sequence
Hard: Transportation Hub
Due:  Tuesday, May 5th, 2026 at 10:00pm