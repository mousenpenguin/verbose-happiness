# BST新增/刪除/查詢/修改功能說明

-   `insert()`新增: 新增節點，依二元搜尋樹的規則排好。
-   `delete()`刪除: 刪除指定的節點，且讓剩下節點依二元搜尋樹的規則排好。
-   `search()`查詢: 搜尋某個節點的數值。
-   `modify()`修改: 這一個想了許久，感覺是把所某個節點之數值改成另一個值，並讓更新後的所有節點依照二元搜尋樹的規則排好。但最後無法寫出。



**Insert**
比節點大，往右走，比節點小，往左走，直到把數值插入。

**Delete**
先找到想刪除的節點，再判斷節點有無子節點，若是沒有，直接刪除。

**Search**
核心部分為比大小，與Insert類似。

**Modify**
同上

Reference:

 1. [http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)
 2. [http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html](http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html)
 3. [https://zh.wikipedia.org/zh-tw/%E4%BA%8C%E5%8F%89%E6%A0%91](https://zh.wikipedia.org/zh-tw/%E4%BA%8C%E5%8F%89%E6%A0%91)
