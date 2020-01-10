# Single-Source Shortest Path：Dijkstra's Algorithm
![enter image description here](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Graph%20series/ShortestPath_fig/SingleSource_Dijkstra/f1.png?raw=true)

![enter image description here](https://s04121155.s3.amazonaws.com/Other+Works/D1.jpg)


![enter image description here](https://s04121155.s3.amazonaws.com/Other+Works/D2.jpg)


**Kruskal (global approach):** At each step, choose the cheapest available edge _anywhere_ which does not violate the goal of creating a spanning tree.

**Dijkstra:** At each step, choose the edge _attached to any previously chosen vertex_ (the local aspect) which makes the _total distance from the starting vertex_ (the global aspect) as small as possible, and does not violate the goal of creating a spanning tree.

**Dijkstra**’s algorithm is used to compute the minimal distance from a node to all the other nodes in a weighted graph.

**Kruskal**’s algorithm are used to compute the minimum spanning tree.

I will a speak about how these two algorithms are different.

We’re assuming a N nodes, M edges undirected connected graph. Choosing in between them depends a lot on the values of N, M and what’s the format in which your graph is given.

**Kruskal**

Starts with a set of N trees. Each tree is comprised of a node. At each step it picks one edge that connects two different trees. This edge is the one with the minimum cost that has not yet been picked.

In order to do this you need to sort the edges and then keep track of the nodes that form each tree. For this you’ll probably want to use a _Disjoint set_ data structure.

--------------------------------

Dijkstra是解決「**單源最短路徑問題**」的算法。這個問題是說，**如何找到從某個特定的節點出發，通向其他節點的最短路徑**。

Example
把城市的路口看作圖的節點，把公路看做邊，綜合長度、擁堵程度等指標作為邊的權重，就可以通過Dijkstra算法計算出從城市一點到另一點的最短路線。


Kruskal則是解決「**最小生成樹問題**」的算法，即**在一個連通的圖里，如何去除圖里的邊，使得剩餘的邊仍能連接所有的節點，且這些邊的權重之和最小**。

Example
有一個快遞公司，每天都要開車把快遞送到城市里的不同地點，怎樣走才能不重複地經過每個節點，還能讓總時間最短呢？我們就可以用Kruskal這樣的最小生成樹算法，找到一個最小生成樹，只需要按這個路線走就行了。


  



