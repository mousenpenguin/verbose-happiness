
# BFS & DFS流程圖：

**BFS 流程**

1.  首先將根節點放入佇列中。
    
2.  從佇列中取出第一個節點，並檢驗它是否為目標：
    
    a. [如果找到目標，則結束搜尋並回傳結果。] b. [否則將它所有尚未檢驗過的直接子節點加入佇列中。]
    
3.  若佇列為空，表示整張圖都檢查過了——亦即圖中沒有欲搜尋的目標。結束搜尋並回傳「找不到目標」。
    
4.  重複步驟2。
    

**DFS流程**

1.  首先將根節點放入stack中。
2.  從stack中取出第一個節點，並檢驗它是否為目標。

> a.[如果找到目標，則結束搜尋並回傳結果。] b.[否則將它某一個尚未檢驗過的直接子節點加入stack中。]

3.  重複步驟2。
4.  如果不存在未檢測過的直接子節點。

> a.[將上一級節點加入stack中。] b.[重複步驟2。]

5.  重複步驟4。
6.  若stack為空，表示整張圖都檢查過了——亦即圖中沒有欲搜尋的目標。結束搜尋並回傳「找不到目標」。

**DFS VS BFS**

在DFS中，　使用佇列儲存節點，而在BFS 中，使用 棧儲存節點。原因就在於二者 優先次序的不同。 佇列是一種先進先出的資料結構，對於每一個節點而言，每一次搜尋，都是優先這一個節點的子節點，所以每一次加入等待序列之後，都要等到某一個節點的所有子節點都被訪問完畢， 才可以進行下一個節點的訪問，這正好是，先進入等待序列 的節點，先出序列進行計算，而後進入的，則後出，所以使用佇列儲存。  
棧是一種先進後出的資料結構，在DFS中，我們要對每一條路徑走到底，才可以回溯前驅節點，所以當節點加入等待序列之後，都要先讓後加入的（也就是子節點中的某一個） 節點先進行運算， 以保證是一條路走到底，所以符合棧的設計。
![enter image description here](https://s04121155.s3.amazonaws.com/Other+Works/DFS.jpg)
![enter image description here](https://s04121155.s3.amazonaws.com/Other+Works/BFS.jpg)
[https://zhuanlan.zhihu.com/p/24986203](https://zhuanlan.zhihu.com/p/24986203)

[https://github.com/zhaoqieyu/LearningNotes/blob/master/HW5/BFS_DFS_%E5%8E%9F%E7%90%86%26%E6%AF%94%E8%BC%83_%E6%B5%81%E7%A8%8B%E5%9C%96_%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.ipynb](https://github.com/zhaoqieyu/LearningNotes/blob/master/HW5/BFS_DFS_%E5%8E%9F%E7%90%86%26%E6%AF%94%E8%BC%83_%E6%B5%81%E7%A8%8B%E5%9C%96_%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.ipynb)

[https://www.educative.io/edpresso/dfs-vs-bfs](https://www.educative.io/edpresso/dfs-vs-bfs)
