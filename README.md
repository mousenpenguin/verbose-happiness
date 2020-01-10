
# Jeff's Learning Note

I hope to further enhance my capabilities of Python and other data forms. With this note I plan to add weekly updates of what I have learned, and the problems that I have encountered. 



## The *End of the Class* UPDATE

Being a double major, it really is a challenge for me to study for this class. My basic Python abilities were very limited, as I was also studying **計算機概論 for freshman**. So you could see how difficult it was for me to learn in this class. Alas, I have truly learned alot from this class, with a much more intimate knowledge of what goes on within the world of stacks and queue, of linked list, of DFSs, of much much more. 我真的希望我能至少**及格**，因為身為**大五**的我，以經沒有時間再等待新一學期的課了，要是這門課不幸被當，我就只能轉成輔系，之前的努力便付諸_流水了。   Thanks again to the professor and the TA for their hard work in teaching this class, you really were some of the most hardworking people I have ever have the pleasure to meet. 

## Personal Information

+ 林玠豪
+ 東吳大學
+ 英文巨資雙主修


### WEEK1
    
-    Moon Festival  放假

### WEEK2

Linked List  
_Linked list_(連結串列)是一種常見的資料結構

[Linked List](https://github.com/mousenpenguin/verbose-happiness/blob/master/Leetcode/707#_Design%20Linked%20List_04121155.py)



### WEEK3

Stack  
基本演算法，像書本一層一層疊上去，Last in First Out  

[Stack](https://github.com/mousenpenguin/verbose-happiness/blob/master/Leetcode/155#_Min%20Stack_04121155.py)

Queue  
基本演算法，像排隊一個一個往後排，First in First Out  

[Queue](https://github.com/mousenpenguin/verbose-happiness/blob/master/Leetcode/232#_Implement%20Queue%20using%20Stacks_04121155.py)

### WEEK4


找重複值和缺失值，老師上課教了一種方式，也提供我們另外5種，我選了一種打在Leetcode，但是他說Time Limit Exceeded  
雖然觀念是對的，但是時間太久了，詳細細節在下面的連結  

[Set](https://github.com/mousenpenguin/verbose-happiness/blob/master/Leetcode/232%23_Implement%20Queue%20using%20Stacks_04121155.py)


### WEEK5

-   放假  (Double Tenth Day)
    
    

### WEEK6

Quick Sort  
往前一個位子比較，比自己大就再往前，比自己小就可以插入，平均時間複雜度高，且不穩定。  



[QuickSortDiagram](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW1/QuickSort%20Diagram.png)
[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW1/Quicksort%20Homework.ipynb)
    

Heap Sort  
想成一個tree的狀態，建立MAX Heap再把最大的root換到最後一個位子。


[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW2/HeapSort.py)
[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW2/HeapSort%20Explain%20and%20Diagram.ipynb)

###WEEK7

Merge Sort  
先將全部的值分成一個一個看，兩組兩組比較，小的擺前，大的擺後。

[HW2](https://github.com/mousenpenguin/verbose-happiness/tree/master/HW2)
[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW2/MergeSort.py)
[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW2/MergeSort%20Explain%20and%20Diagram.ipynb)
### WEEK8

Binary Tree  
從root開始，每個node可以有兩個child，位子比較前的接兩個child後，才會換下個接  
root是parent。



### WEEK9

Binary Search Tree  
（1）若左子樹不空，則左子樹上所有結點的值均小於它的根結點的值；

（2）若右子樹不空，則右子樹上所有結點的值均大於它的根結點的值；

（3）左、右子樹也分別為二元查找樹

[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW3/binary_search_tree_04121155.py)

[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW3/binary_search_tree%20explain.md)

[Process](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW3/binary_search_tree%20learning%20process.ipynb)



### WEEK10

Red Black Tree  
非常困難，比Binary Search Tree多了平衡，新增要平衡，刪除也要平衡  



### WEEK11

Hash Table  
是根據關鍵碼值(Key value)而直接進行訪問的數據結構。也就是說，它通過把關鍵碼值映射到表中一個位置來訪問記錄，以加快查找的速度。這個映射函數叫做散列函數(hash function)，存放記錄的數組叫做散列表。如果數對p的關鍵字是k，哈希函數為f，那麼在理想情況下，p在哈希表中的位置就是f(k)。 

[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW4/hash_table_04121155.py)

[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW4/hash_table_%E6%B5%81%E7%A8%8B%E5%9C%96_%E6%AD%B7%E7%A8%8B_%E5%8E%9F%E7%90%86.md)


### WEEK12

Breadth-First Search  
**廣度優先搜尋法**，是一種圖形(graph)搜索演算法。從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。
[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW5/BFS_04121155.py)

[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW5/BFS,DFS%20%E6%B5%81%E7%A8%8B%E5%9C%96%EF%BC%8C%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%EF%BC%8C%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83.md)
  

### WEEK13

Depth-First Search  
**深度優先搜尋法**，是一種用來遍尋一個樹(tree)或圖(graph)的演算法。由樹的根(或圖的某一點當成 根)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目 的節點或遍尋全部節點。

[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW5/BFS_04121155.py)

[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW5/BFS,DFS%20%E6%B5%81%E7%A8%8B%E5%9C%96%EF%BC%8C%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%EF%BC%8C%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83.md)



### WEEK14

Minimum Spanning Tree  

**About Dijkstra**
Dijkstra使用了廣度優先搜尋(BFS)解決賦權有向圖的單源最短路徑問題(shortest path)，主要是利用兩點間的權重路徑，找出各點距離起點的最短路徑。
[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW6/Dijkstra_04121155.py)

[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW6/Dijkstra%E8%88%87Kruskal%20%E6%B5%81%E7%A8%8B%E5%9C%96%EF%BC%8C%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%EF%BC%8C%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83.md)



### WEEK15

Shortest Path  

**About Kruskal**
Kruskal是一種用來尋找最小生成樹(minimum spanning tree)的演算法。
[Code](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW6/Dijkstra_04121155.py)

[Explain](https://github.com/mousenpenguin/verbose-happiness/blob/master/HW6/Dijkstra%E8%88%87Kruskal%20%E6%B5%81%E7%A8%8B%E5%9C%96%EF%BC%8C%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%EF%BC%8C%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83.md)



### WEEK 16

-   Overview

### WEEK17

-   Final

### WEEK18

 - **VOTE!!!**




    
