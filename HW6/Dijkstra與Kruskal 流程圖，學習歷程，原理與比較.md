# Single-Source Shortest Path：Dijkstra's Algorithm
![enter image description here](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Graph%20series/ShortestPath_fig/SingleSource_Dijkstra/f1.png?raw=true)

![enter image description here](https://s04121155.s3.amazonaws.com/Other+Works/D1.jpg)


![enter image description here](https://s04121155.s3.amazonaws.com/Other+Works/D2.jpg)


**Kruskal (global approach):** At each step, choose the cheapest available edge _anywhere_ which does not violate the goal of creating a spanning tree.

**Dijkstra:** At each step, choose the edge _attached to any previously chosen vertex_ (the local aspect) which makes the _total distance from the starting vertex_ (the global aspect) as small as possible, and does not violate the goal of creating a spanning tree.

**Dijkstra**’s algorithm is used to compute the minimal distance from a node to all the other nodes in a weighted graph.

**Kruskal**’s algorithm are used to compute the minimum spanning tree.

I will a bit about how these two algorithms are different.

We’re assuming a N nodes, M edges undirected connected graph. Choosing in between them depends a lot on the values of N, M and what’s the format in which your graph is given.

**Kruskal**

Starts with a set of N trees. Each tree is comprised of a node. At each step it picks one edge that connects two different trees. This edge is the one with the minimum cost that has not yet been picked.

In order to do this you need to sort the edges and then keep track of the nodes that form each tree. For this you’ll probably want to use a _Disjoint set_ data structure.

