[Quick Sort (快速排序)](https://en.wikipedia.org/wiki/Quicksort)，是一種 divide and conquer 的排序方法，其過程如下：

 1.  先從 array 中選出一個元素當基準 (pivot)，然後讓 pivot 左邊的元素都小於 pivot，pivot 右邊的元素都大於等於 pivot。（先不用排序）。
 2.  分別對左邊的 array 和右邊的 array 重複這個過程。
-----------------------------------------------------------

1. 取第一個元素（最左的數）為鍵值 key

2. 由左向右（前向後）找一個數（第一個滿足的），

其值大於等於 key 值，該數之索引為 left_pivot

3. 由右向左（後向前）找一個數（第一個滿足的），

其值小於等於 key 值，該數之索引為 right_pivot

4. 如果 left_pivot < right_pivot 則交換值，

否則把 key 值與 right_pivot 值交換，以 right_pivot 為基準，分為左右兩個數列

5. 重複上述步驟排序左右兩個數列，直到完成排序
