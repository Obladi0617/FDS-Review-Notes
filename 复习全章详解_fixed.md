# 数据结构与算法（第2–第9章） — 详解版

说明：本文件为扩展版。每章包含：概念要点、推导/证明、关键算法的伪代码或 C 代码示例、典型例题与逐步解析、练习题与答案提示。适合期中冲刺与刷题训练。

---

## 目录（快速跳转）
- 第2章 算法分析（渐进表示、主定理、常见递推）
- 第3章 栈与队列（实现、表达式、应用）
- 第4章 树与二叉树（遍历、重建、表达式树）
- 查找树（BST：查找/插入/删除/复杂度）
- 第5章 优先队列（堆：上/下滤、建堆证明）
- 并查集（Union-Find）与线段树（建树/查询/更新）
- 第9章 图算法（BFS/拓扑/Dijkstra/Bellman-Ford）
- 常见题型汇总与真题例析
- 附录：练习题与完整解析

---

## 第2章 算法分析


### 1) 渐进符号与定义（极细致讲解）

- **上界 O(f(n))**：表示 T(n) 增长不会超过 f(n) 的常数倍。形式化：存在常数 c>0 和 n0，使得对所有 n≥n0，有 T(n) ≤ c·f(n)。
  - 例：T(n)=3n+7，T(n)=O(n)。取 c=4, n0=7 即可。
  - 常见误区：O(f(n)) 不是等于，而是“至多如此快”。
- **下界 Ω(f(n))**：T(n) 至少增长和 f(n) 一样快。存在 c>0, n0，使得 T(n) ≥ c·f(n)。
  - 例：T(n)=2n+1，T(n)=Ω(n)。
- **同阶 Θ(f(n))**：T(n) 既是 O(f(n)) 又是 Ω(f(n))，即增长速度与 f(n) 完全一致。
  - 例：T(n)=5n+2，T(n)=Θ(n)。

> **常见问题**：
> - 为什么要用渐进符号？答：屏蔽常数与低阶项，关注大规模输入下的本质效率。
> - O(n^2) 算法和 O(n) 算法哪个快？答：理论上 n 足够大时 O(n) 更快，但实际还要看常数和实现。

#### 相关符号
- o(f(n))：严格小于 O(f(n))，即 T(n)/f(n) → 0。
- ω(f(n))：严格大于 Ω(f(n))，即 T(n)/f(n) → ∞。

#### 典型陷阱
- O(f(n)) 不是唯一界，T(n)=O(n^2) 也等于 O(n^3)，但我们总选最紧的。
- 证明 O/Ω/Θ 时要写出常数和 n0。

---


### 2) 常见复杂度例子与增长对比

- O(1)：常数时间，如数组下标访问。
- O(log n)：对数时间，如二分查找。
- O(n)：线性时间，如遍历数组。
- O(n log n)：归并/快速排序。
- O(n^2)：双重循环，如冒泡排序。
- O(2^n)：指数级，如递归解子集。

> **增长快慢口诀**：常数 < 对数 < 线性 < 线性对数 < 多项式 < 指数 < 阶乘。

#### 例题：
判断下列哪个增长最快？A. n log n  B. n^2  C. 2^n  D. n!
答案：D > C > B > A。

---


### 3) 递推与主定理（详细推导）

主定理用于求解形如 T(n)=aT(n/b)+f(n) 的递归：
- a：子问题个数
- b：每个子问题规模缩小倍数
- f(n)：分解/合并的额外工作

令 c=log_b a，分三类：

1. f(n) = O(n^{c-ε})，递归主导，T(n)=Θ(n^c)
2. f(n) = Θ(n^c log^k n)，平衡，T(n)=Θ(n^c log^{k+1} n)
3. f(n) = Ω(n^{c+ε}) 且正则性，T(n)=Θ(f(n))


> **推导例子**：
> - T(n)=2T(n/2)+n，a=2,b=2,f(n)=n，c=1，f(n)=Θ(n^1)，第二类，T(n)=Θ(n log n)
> - T(n)=4T(n/2)+n，a=4,b=2,c=2，f(n)=n=O(n^{2-ε})，第一类，T(n)=Θ(n^2)

#### 常见递推解法
- 展开法：多次代入，找规律。
- 画递归树：每层工作量相加。

---


### 4) 例题与逐步解析（极细致）

#### 例题 2.1（平方根循环）
代码：
```c
int x=0;
while(n>=(x+1)*(x+1)) x++;
```
分析：每次循环 x 增 1，直到 (x+1)^2>n。解不等式得 x<√n，循环次数约 √n 次。
**易错点**：有同学误以为是 O(n)，实际每次 x 增 1，增长远慢于 n。
**变式**：若 x*=2，每次乘 2，则循环次数为 O(log n)。

#### 例题 2.2（递推主定理）
P1: T(1)=1, T(N)=T(N/3)+1
分析：每次规模缩小 1/3，递归深度 log_3 N，每层 O(1)，总 O(log N)。
P2: T(1)=1, T(N)=3T(N/3)+1
分析：每层分 3 个子问题，递归树每层工作量 3^k，深度 log_3 N，总和 O(N)。

#### 例题 2.3（复杂度比较）
题：比较 N log N、N^2、2^N、N! 的增长。
解：N! > 2^N > N^2 > N log N。
**技巧**：多项式 < 指数 < 阶乘。

#### 例题 2.4（素数判定复杂度）
朴素做法：for i=3 到 N，O(N)。若只到 √N，O(√N)。
**易错点**：题目若未说明优化，只能按 O(N) 算。

#### 例题 2.5（递归空间）
递归 Fibonacci：每次递归深度 N，空间 O(N)。
**补充**：若用循环或记忆化，空间可降到 O(1) 或 O(N)。

---

---

## 第3章 栈与队列（详解）

### 栈（Stack）
- ADT：Push/Pop/Top/IsEmpty。
- 常见实现：数组（顺序栈）与链表（链式栈）。

数组栈示例（C）：

```c
typedef struct { int *a; int top; int cap; } Stack;
Stack* newStack(int cap){ Stack*s=malloc(sizeof* s); s->a=malloc(sizeof(int)*cap); s->top=-1; s->cap=cap; return s; }
void push(Stack*s,int v){ if(s->top+1<s->cap) s->a[++s->top]=v; }
int pop(Stack*s){ return s->a[s->top--]; }
int isEmpty(Stack*s){ return s->top==-1; }
```

时间：Push/Pop O(1)。

应用 1：括号匹配（逐字符处理，栈顶匹配即可）。

应用 2：表达式处理（中缀、后缀、前缀）详细讲解

### A. 三种表达式形式
- 中缀（Infix）：`a + b * c`，人类最常用，需要括号和优先级规则。
- 后缀（Postfix, 逆波兰）：`a b c * +`，机器求值方便，不需要括号。
- 前缀（Prefix）：`+ a * b c`，同样不需要括号。

核心目标：

1. 中缀转后缀（考试高频）
2. 后缀表达式求值（代码题高频）


### B. 运算符优先级与结合性
常见优先级（高到低）：
1. `()`
2. `^`（幂，通常右结合）
3. `* / %`（左结合）
4. `+ -`（左结合）

左结合的含义：`a-b-c` 按 `(a-b)-c`。
右结合的含义：`a^b^c` 按 `a^(b^c)`。

### C. 中缀转后缀（栈法）完整规则
扫描中缀表达式 token（数字、变量、运算符、括号）：

1. 若是操作数（数字/变量），直接输出到后缀序列。
2. 若是左括号 `(`，入栈。
3. 若是右括号 `)`，反复弹栈并输出，直到遇到 `(`，再弹出 `(` 丢弃。
4. 若是运算符 op：
   - 当栈顶也是运算符，且“栈顶优先级更高”或“优先级相等且 op 为左结合”，就弹出栈顶到输出。
   - 然后把 op 入栈。
5. 扫描结束后，把栈内剩余运算符全部弹出到输出。

伪代码（可直接背）：

```text
for token in expr:
  if token is operand:
    output token
  else if token == '(':
    push(token)
  else if token == ')':
    while top() != '(':
      output pop()
    pop() // 丢弃 '('
  else: // token 是运算符 op
    while stack not empty and top is operator and (
          prec(top) > prec(op)
          or (prec(top) == prec(op) and op is left-associative)):
      output pop()
    push(op)

while stack not empty:
  output pop()
```

### D. 逐步示例 1（无括号）
中缀：`a + b * c - d / e`

逐 token 过程（输出序列记作 out，运算符栈记作 st）：

1. 读 `a`：out=`a`，st=`[]`
2. 读 `+`：out=`a`，st=`[+]`
3. 读 `b`：out=`a b`，st=`[+]`
4. 读 `*`：`*` 优先级高于 `+`，直接入栈。out=`a b`，st=`[+, *]`
5. 读 `c`：out=`a b c`，st=`[+, *]`
6. 读 `-`：比较栈顶 `*`，`*` 优先级高，弹出。out=`a b c *`，st=`[+]`
7. 继续比较栈顶 `+`，与 `-` 同级且左结合，弹出。out=`a b c * +`，st=`[]`
8. 把 `-` 入栈：out=`a b c * +`，st=`[-]`
9. 读 `d`：out=`a b c * + d`，st=`[-]`
10. 读 `/`：`/` 高于 `-`，入栈。out=`a b c * + d`，st=`[-, /]`
11. 读 `e`：out=`a b c * + d e`，st=`[-, /]`
12. 扫描结束，弹栈：先 `/` 再 `-`


最终后缀：`a b c * + d e / -`

### E. 逐步示例 2（含括号）
中缀：`(a+b) * (c-d)`

过程要点：
- 遇到 `(` 只入栈，不输出。
- 遇到 `)` 时一直弹出到 `(`。

最终后缀：`a b + c d - *`

### F. 后缀表达式求值（数值题）
规则：

1. 扫描 token。
2. 若是数字，入栈。
3. 若是运算符，从栈顶弹出两个数：先弹的是右操作数 rhs，再弹的是左操作数 lhs。
4. 计算 `lhs op rhs`，结果入栈。
5. 扫描结束，栈顶即答案。


伪代码：

```text
for token in postfix:
  if token is number:
    push(token)
  else:
    rhs = pop()
    lhs = pop()
    push(apply(lhs, token, rhs))
return pop()
```

示例：

1. push 3, push 4, push 2
2. `*` => 4*2=8，push 8
3. `+` => 3+8=11，push 11
4. push 7
5. `-` => 11-7=4
结果：4


### G. C 语言实现模板（考试可改写）

```c
// 仅演示核心逻辑：中缀转后缀（token 已拆分）
int prec(char op){
    if(op=='+'||op=='-') return 1;
    if(op=='*'||op=='/'||op=='%') return 2;
    if(op=='^') return 3;
    return 0;
}
int is_left_assoc(char op){ return op!='^'; }

// 若 token 是单字符运算符/括号或操作数，按规则处理
// 实际工程中需支持多位数、空格、负号和非法输入校验
```

### H. 高分易错点总结
1. **弹栈条件写错**：同优先级时是否弹栈取决于结合性。
2. **后缀求值操作数顺序错**：应为 `lhs op rhs`，不是反过来。
3. **括号处理遗漏**：遇 `)` 必须弹到 `(`；最后不能把 `(` 输出。
4. **一元负号处理**：`-5` 与 `3-5` 含义不同，严格实现时需在词法阶段区分。
5. **多位数字切分错误**：`123` 应视作一个 token，不是 `1 2 3`。

### I. 变式与应试技巧
1. 若题目要“中缀转前缀”：可先反转中缀并交换括号，再按中缀转后缀规则处理，最后反转结果。
2. 若题目给“表达式树”：后缀转树最方便，遇操作数建叶子，遇运算符弹出两棵子树组合。
3. 手算时推荐画两列：`输出序列` 与 `运算符栈`，每一步都写，基本不丢分。

### J. 练习题（含详解）
以下练习覆盖中缀→后缀（含结合性/括号）、多位数 token、后缀求值和中缀→前缀变式。

例题 3.1（中缀→后缀，优先级与右结合）
中缀：`a + b * (c ^ d ^ e) - f / g`

逐步（out=输出，st=运算符栈）：

1. a → out=`a`, st=`[]`
2. + → st=`[+]`
3. b → out=`a b`
4. * → st=`[+, *]`
5. ( → st=`[+, *, (]`
6. c → out=`a b c`
7. ^ → st=`[+, *, (, ^]`（右结合，遇同级不弹）
8. d → out=`a b c d`
9. ^ → st=`[+, *, (, ^, ^]`
10. e → out=`a b c d e`
11. ) → 弹出到 `(`：先弹 `^`,`^` → out=`a b c d e ^ ^`，然后丢弃 `(`，st=`[+, *]`
12. - → 先弹 `*` (高于 `-`) → out=`a b c d e ^ ^ *`，再弹 `+` (同级且左结合) → out=`a b c d e ^ ^ * +`，入栈 `-`
13. f → out=`a b c d e ^ ^ * + f`
14. / → st=`[-, /]`
15. g → out=`a b c d e ^ ^ * + f g`
16. 扫描结束，弹 `/`、`-` → 最终后缀：`a b c d e ^ ^ * + f g / -`


例题 3.2（多位数与括号）
中缀：`12 + 34 * (5 - 2)`
解析：token 为 `12`,`+`,`34`,`*`,`(`,`5`,`-`,`2`,`)`，按规则得后缀：`12 34 5 2 - * +`。

例题 3.3（中缀→前缀，反转法）
中缀：`a + (b - c) * d`
步骤（技巧）：反转并交换括号得到 `d * (c - b) + a`，对其做中缀→后缀得 `d c b - * a +`，再反转得到前缀：`+ a * - b c d`。

例题 3.4（后缀求值）
后缀：`5 1 2 + 4 * + 3 -`
过程（栈顶右侧为最新）：

1. push 5 → [5]
2. push 1 → [5,1]
3. push 2 → [5,1,2]
4. `+` → pop 2,1 → 3 → push → [5,3]
5. push 4 → [5,3,4]
6. `*` → pop 4,3 → 12 → push → [5,12]
7. `+` → pop 12,5 → 17 → push → [17]
8. push 3 → [17,3]
9. `-` → pop 3,17 → 14 → push → [14]
答案：14


---

### 队列（Queue）
- 循环队列注意 front/rear 更新与满/空判定（计数或空一位法）。
- BFS 使用队列求无权最短路，复杂度 O(|V|+|E|)。

练习：数组长度 6，front=0,rear=4，2 次 dequeue 后 front=2；2 次 enqueue 后 rear=(4+2)%6=0。

---

## 第4章 树与二叉树（详解）

### 术语
- 节点、根、子树、叶子、深度/高度、度。

### 遍历
- 前序/中序/后序/层序（BFS）。递归实现最直接。

### 重建二叉树（关键题型）
算法（前序+中序）：前序第一为根，在中序中划分左右子树，递归重建。

示例（完整步算）：
前序 [A B D E C F], 中序 [D B E A F C]
根=A；中序左=[D B E], 右=[F C]；前序对应左=[B D E], 右=[C F]。递归下去即可。

练习题：实践对小序列手写重建并验证遍历序列一致。

### 线索二叉树（Threaded Binary Tree）

引言：普通二叉树中大量空指针既浪费空间，又在遍历时需要使用栈或递归。线索二叉树利用这些空指针存放某种遍历序列中的前驱或后继（称为“线索”），从而实现无需栈和递归的顺序访问。

节点定义（常见实现）：

```c
typedef struct ThreadNode {
  int val;
  struct ThreadNode *l, *r;
  int ltag; // 0 表示 l 指向左孩子，1 表示 l 为前驱线索
  int rtag; // 0 表示 r 指向右孩子，1 表示 r 为后继线索
} ThreadNode;
```

线索的分类：
- 按遍历顺序：前序线索、**中序线索（最常见）**、后序线索。
- 按线索数量：单线索（二叉树只用左或右线索）与双线索（左右都做线索）。

中序线索的构造（常考）——思路：在中序遍历过程中维护一个指针 `pre`（指向前一个已访问结点），
- 若当前结点 p 的左指针为空，则令 p->l = pre，p->ltag = 1（左线索指向前驱）；
- 若 pre 存在且 pre->r 为空，则令 pre->r = p，pre->rtag = 1（pre 的右线索指向后继 p）；
- 更新 pre = p，继续递归右子树。

递归实现模板：

```c
void InThread(ThreadNode *p, ThreadNode **pre) {
  if (p) {
    InThread(p->l, pre);
    if (!p->l) { p->l = *pre; p->ltag = 1; }
    if (*pre && !(*pre)->r) { (*pre)->r = p; (*pre)->rtag = 1; }
    *pre = p;
    InThread(p->r, pre);
  }
}

void CreateInorderThread(ThreadNode *root) {
  ThreadNode *pre = NULL;
  InThread(root, &pre);
  if (pre) { pre->r = NULL; pre->rtag = 1; }
}
```

中序遍历（利用线索，常见写法）：

```c
void InOrderThreadTraverse(ThreadNode *root) {
  ThreadNode *p = root;
  // 找到最左侧结点
  while (p && p->ltag == 0) p = p->l;
  while (p) {
    visit(p);
    if (p->rtag == 1) p = p->r; // 直接跳到后继
    else {
      p = p->r; // 进入右子树，继续走到该子树最左结点
      while (p && p->ltag == 0) p = p->l;
    }
  }
}
```

小例子说明：
给定二叉树
```text
  2
 / \
1   3
```
中序访问序列为 `1 2 3`。建立中序线索后：
- `1.r -> 2`（1 的右指针作为线索指向后继 2），`1.rtag = 1`；
- `2.l` 依旧为左孩子 1，`2.ltag = 0`；`2.r` 指向右孩子 3，`2.rtag = 0`；
- `3.l -> 2`（3 的左指针作为线索指向前驱 2），`3.ltag = 1`。

优缺点与应用：
- 优点：遍历时无需额外栈或递归，适合顺序访问场景；能快速得到结点在中序下的前驱/后继。
- 缺点：插入/删除需要更新大量线索，维护复杂；实现与调试难度较常规树高。
- 应用：适用于读多写少、需要频繁中序遍历或查找前驱/后继的场景。

练习题（第4章 线索二叉树）
1) 给定一棵二叉树（画图），请画出中序线索后的指针指向并写出每个结点的 `ltag/rtag` 值。
2) 请实现 `CreateInorderThread` 的非递归版本（提示：使用显式栈模拟中序遍历，同时维护 `pre`）。
3) 已知一个线索二叉树的 `ltag/rtag` 与指针关系，按中序写出结点序列（手算）。

---

### 参考答案与实现要点

下面给出练习题的要点提示与一份非递归实现参考，便于你校对与复现。

1) 题解要点（画图题）
- 步骤：先写出该树的中序遍历序列（递归或手算），然后按中序遍历顺序把前驱/后继连接起来：对于序列中的每个结点 v，其前驱为序列中前一个元素，后继为后一个元素；若某结点本来有左/右孩子，则对应指针保留孩子关系并把 ltag/rtag 设为 0，否则将指针改为线索并把相应的 tag 设为 1。
示例（快速）：对
```text
  2
 / \
1   3
```
中序序列 `1,2,3`，因此 1 的后继为 2（`1.r->2` 且 `1.rtag=1`），3 的前驱为 2（`3.l->2` 且 `3.ltag=1`），2 的左右仍为孩子，`2.ltag=0,2.rtag=0`。

2) 非递归 `CreateInorderThread` 参考实现（C 风格）

```c
// 非递归中序线索化（使用显式栈）
void CreateInorderThreadNonRec(ThreadNode *root) {
  if (!root) return;
  // 简单静态栈示例，真实代码中请用动态数组或链式栈以避免越界
  ThreadNode *stack[256];
  int top = 0;
  ThreadNode *p = root;
  ThreadNode *pre = NULL;

  while (p || top > 0) {
    while (p) { stack[top++] = p; p = p->l; }
    p = stack[--top]; // 访问该结点
    if (!p->l) { p->l = pre; p->ltag = 1; }
    if (pre && !pre->r) { pre->r = p; pre->rtag = 1; }
    pre = p;
    p = p->r;
  }
  if (pre) { pre->r = NULL; pre->rtag = 1; }
}
```

注意点：
- 使用显式栈模拟中序遍历，处理逻辑与递归版本一致；注意在设置线索时只在对应孩子指针为空时设置，并相应置 tag。
- 栈大小需根据树高估算或使用动态结构以防溢出。

3) 题 3（根据线索写出中序序列）要解法提示
- 找到中序的最左结点（从任意根开始，沿左子指针直到 `ltag==1` 或 NULL），然后按线索遍历规则依次输出：若 `rtag==1`，直接跳到 `r`；否则进入右子树并继续走到该子树最左结点。

示例答案（快速手算）：若给定线索关系展示为 `A` 的后继为 `C`、`C` 的前驱为 `A` 等，按上述规则即可复原完整序列。

---

## 查找树（BST）
### 操作与实现要点（详解）

BST（Binary Search Tree）性质：对任意节点 v，左子树所有键 < v->key，右子树所有键 > v->key；中序遍历得到升序序列。

复杂度：查找/插入/删除平均 O(log n)，最坏退化为链表 O(n)。是否平衡决定性能（AVL/红黑树为平衡 BST，课外可扩展）。

常用操作模板（递归实现）：

```c
Node* find(Node* t,int x){
  if(!t) return NULL;
  if(x==t->val) return t;
  return x < t->val ? find(t->left,x) : find(t->right,x);
}
Node* insert(Node* t,int x){
  if(!t) return newNode(x);
  if(x < t->val) t->left = insert(t->left,x);
  else if(x > t->val) t->right = insert(t->right,x);
  return t;
}
```

删除（三种情况）详解：

1. 节点为叶子：直接 free 并把父指针置 NULL。
2. 节点度为 1：把父指针指向唯一子节点并释放当前节点。
3. 节点度为 2：找到右子树的最小节点（inorder successor）或左子树最大节点（inorder predecessor），用该节点的值替换当前节点值，然后在对应子树中删除那个替换节点（该替换节点度 ≤ 1）。


删除递归实现（以右子树最小替换）：

```c
Node* findMin(Node* t){ while(t->left) t = t->left; return t; }
Node* delete(Node* t,int x){
  if(!t) return NULL;
  if(x < t->val) t->left = delete(t->left,x);
  else if(x > t->val) t->right = delete(t->right,x);
  else {
    if(!t->left){ Node* r=t->right; free(t); return r; }
    else if(!t->right){ Node* l=t->left; free(t); return l; }
    else {
      Node* m = findMin(t->right);
      t->val = m->val;
      t->right = delete(t->right,m->val);
    }
  }
  return t;
}
```

逐步示例（删除度为 2 的节点）：
给定 BST，删除根节点 10（假设存在左右子树）。步骤：找到 10 的右子树最小值 say 12；把 12 的值赋给根，递归在右子树删除原来的 12 节点（其度 ≤ 1），最终树结构调整完成。

迭代版本与父指针维护：考试题可能要求不使用递归，需用循环和父指针跟踪替换点并手动调整链接。

其他常考点：
- 求中序后继/前驱：若右子树存在，则后继为右子树最小；否则向上找第一个把当前结点放在左子树位置的祖先。
- 判断某插入序列是否能生成给定 BST：模拟插入或用二叉搜索树性质约束。

练习题（BST 深化）
1) 给插入序列 [8,3,10,1,6,14,4,7,13]，画出 BST，并写出删除 3 后的先序遍历结果（提示：用右子树最小替换）。
2) 实现 `findSuccessor(Node* t)`（若存在右子树返回右子树最小，否则向上查找祖先）。
3) 讨论在 BST 中实现 `delete` 的迭代版本时需要维护哪些父指针，并写出关键伪代码段。

---
---

## 第5章 优先队列（堆）
## 第5章 优先队列（堆）

本章细化：数组表示、上滤/下滤的 C 实现、线性建堆（BuildHeap）逐步演算、复杂度证明要点、常见题与练习（含答案提示）。

### 1) 基本定义与数组索引
- 二叉堆（最小堆）满足：完全二叉树结构 + 堆序（父 ≤ 子）。
- 数组下标（1-based）常见约定：父(i)=i/2，左=2i，右=2i+1。
- 注意：实现时要明确是 0-based 还是 1-based，考试题通常用 1-based 表示，写程序时更常用 0-based（对应关系需变换）。

### 2) 插入（上滤 percolateUp）与删除最小（下滤 percolateDown）

要点：尽量用赋值移动（将空位向上/下移动）以减少交换次数。

插入（赋值上滤）示例代码：

```c
void insertHeap(int H[], int *size, int X) {
  int i = ++(*size);
  while (i > 1 && H[i/2] > X) {
    H[i] = H[i/2];
    i /= 2;
  }
  H[i] = X;
}
```

删除最小（下滤）示例代码：

```c
int deleteMin(int H[], int *size) {
  int min = H[1];
  int last = H[(*size)--];
  int i = 1, child;
  while (2*i <= *size) {
    child = 2*i;
    if (child != *size && H[child+1] < H[child]) child++;
    if (last > H[child]) {
      H[i] = H[child];
      i = child;
    } else break;
  }
  H[i] = last;
  return min;
}
```

复杂度：插入与删除最小均为 O(log n)。

### 3) BuildHeap（线性建堆）

算法：从最后一个非叶节点 `i = floor(n/2)` 向下对每个节点执行 `percolateDown`。

伪代码：

```c
void buildHeap(int H[], int n) {
  for (int i = n/2; i >= 1; --i) percolateDown(H, i, n);
}
```

线性时间直观证明要点：深度为 h 的节点数量约为 n/2^{h+1}，每个节点下滤成本 O(h)，求和 Σ h·(n/2^{h+1}) = O(n)（因为 Σ h/2^h 为常数）。

### 4) 逐步示例（完整手算）
给定初始数组（1-indexed）：
`[15,26,32,8,7,20,12,13,5,19]`（n=10）

从 i=5 开始向下处理：
- i=5 (7)：子节点 10=19，7 ≤ 19，无改动。
- i=4 (8)：子 8=13, 9=5，最小子为 9(5)，8>5 ⇒ 交换位置，结果局部变为 ... 5 ... 8 ...
- i=3 (32)：子 6=20,7=12，最小子 7(12)，32>12 ⇒ 置换，32 下沉。
- i=2 (26)：子 4 与 5 的当前值为 5 和 7，最小为 4(5)，26 下沉并继续比较，最终把 26 移到合适位置。
- i=1 (15)：与子节点比较并下滤，最终根变为最小元素 5。

最终建堆结果（手算）：
`[5,7,12,8,15,20,32,13,26,19]`（1-indexed）

插入 6 的过程（上滤）：在末尾插入 6（索引 11），与父 15、7 比较并上移，结果：
`[5,6,12,8,7,20,32,13,26,19,15]`。

练习题解析可基于上述步骤逐步展开，考试时写出关键交换或赋值步骤即可得分。

### 5) 应用、变式与常见考点
- 使用堆实现优先队列（Dijkstra、事件驱动模拟、Top-K）。
- heapify（BuildHeap）与重复调用 `insert` 的差别：前者 O(n)，后者 O(n log n)。可用具体 n 估算对比。
- 注意索引偏移（0-based vs 1-based）和父/子计算的整除行为。

常见易错点：
- 下滤/上滤的边界条件（`child != size` 判断，防止越界）。
- 忘记在插入时更新 `size` 或在删除时先取 `last` 值。

### 6) 练习题（含答案提示）
1) 对数组 `[15,26,32,8,7,20,12,13,5,19]` 做线性建堆，给出每次关键下滤结果与最终堆。答案见上：最终 `[5,7,12,8,15,20,32,13,26,19]`。
2) 在上述堆上插入 `6`，写出上滤过程与最终数组。答案见上：`[5,6,12,8,7,20,32,13,26,19,15]`。
3) 证明 BuildHeap 为 O(n)：给出递归树或层次计数的证明要点（提示：Σ h·n/2^{h} 为常数×n）。
4) 若把数组按 0-based 存储，父/子关系如何调整？（答：父=(i-1)/2，左=2*i+1，右=2*i+2）。

---
---

## 并查集（Union-Find）与线段树（详解）
### A. 并查集（Union-Find）详解

1) 表示与约定
- 常用数组 `parent[]` 表示：若 `parent[x] < 0` 则 x 为根，且 `-parent[x]` 为集合大小；否则 `parent[x]` 为 x 的父结点索引。

2) 操作与优化
- `Find(x)`：返回 x 的根。路径压缩（path compression）在查找时把沿途结点直接指向根。
- `Union(a,b)`：按集合大小（或秩 rank）把小集合根挂到大集合根下面并更新大小/秩。

3) 代码（递归路径压缩 + 按大小合并，1-based 索引示例）：

```c
int Find(int x, int parent[]) {
  return parent[x] < 0 ? x : parent[x] = Find(parent[x], parent);
}
void Union(int a, int b, int parent[]) {
  a = Find(a, parent);
  b = Find(b, parent);
  if (a == b) return;
  // parent[root] 存放 -size
  if (parent[a] < parent[b]) { // |a| > |b|
    parent[a] += parent[b];
    parent[b] = a;
  } else {
    parent[b] += parent[a];
    parent[a] = b;
  }
}
```

4) 摊还复杂度
- 采用路径压缩 + 按秩/大小合并后，任何 m 个操作的总时间近似为 O(m α(n))，α(n) 为逆 Ackermann 函数，增长极慢，接近常数。

5) 示例演练（手算）
- 初始 `parent = {-4, 1, 1, 1, -3, 4, 4, 8, -2}`（示例需按 1-based 或 0-based 规范重写，考试题通常明确）。
- 执行 `union(6,8)`：先 `Find(6)` → r6，`Find(8)` → r8，比较集合大小并把小集合根指向大集合根，更新负大小值。

6) 常见考点与易错点
- 题目常考：给定 parent 数组，执行若干 union 操作后输出数组；或给 parent 数组求某对元素是否连通。
- 易错点：混淆负值含义（是 -size 而非父索引），路径压缩后数组值并非父索引而可能是负数（根）。

---

### B. 线段树（Segment Tree）详解

1) 功能与表示
- 线段树用于区间查询（区间和/最小/最大）与点/区间更新。常用数组 `tree[4*n]` 存树节点信息。

2) 基本操作（区间和示例）
- `build(node,l,r)`：若 `l==r` 则 `tree[node]=A[l]`，否则 `mid=(l+r)/2` 递归构建左右子树并 `tree[node]=tree[left]+tree[right]`。
- `query(node,l,r,qL,qR)`：按区间重叠判断递归或直接返回节点值。
- `update(node,l,r,idx,val)`：点更新或区间更新（无懒惰标记）递归更新并回溯合并。

3) 代码模板（区间和，递归实现，1-based 数组示例）

```c
void build(int node,int l,int r,int A[],int tree[]) {
  if (l==r) { tree[node]=A[l]; return; }
  int m=(l+r)/2;
  build(node*2,l,m,A,tree);
  build(node*2+1,m+1,r,A,tree);
  tree[node]=tree[node*2]+tree[node*2+1];
}
int query(int node,int l,int r,int ql,int qr,int tree[]) {
  if (ql>r || qr<l) return 0; // 不重叠
  if (ql<=l && r<=qr) return tree[node];
  int m=(l+r)/2;
  return query(node*2,l,m,ql,qr,tree)+query(node*2+1,m+1,r,ql,qr,tree);
}
void update(int node,int l,int r,int idx,int val,int tree[]) {
  if (l==r) { tree[node]=val; return; }
  int m=(l+r)/2;
  if (idx<=m) update(node*2,l,m,idx,val,tree);
  else update(node*2+1,m+1,r,idx,val,tree);
  tree[node]=tree[node*2]+tree[node*2+1];
}
```

4) Lazy Propagation（区间更新）
- 当要做区间加/赋值时，使用 `lazy[node]` 存延迟标记，避免访问整个子树。
- 更新和查询时要先 `pushDown(node)` 把标记下传到子节点并更新子节点值。

推迟标记示例（伪代码）：

```text
pushDown(node):
  if lazy[node] != 0:
  apply lazy to children and update their lazy markers
  lazy[node]=0
```

5) 例子（A=[7,2,5,8,3], 1-based）
- Build 后 `query(2,4)` = 2+5+8 = 15。
- 若 `update(3,9)`（点更新），则 A 变为 [7,2,9,8,3]，`query(2,4)` = 2+9+8 = 19。

6) 常见考点与易错点
- 题型：区间求和、区间最大/最小、区间加/乘/赋值（需 lazy）、区间反转/翻转（需维护额外信息）。
- 易错点：数组下标偏移（1-based vs 0-based）、pushDown 写错顺序、合并子节点时使用错误运算。

### 练习题（并查集 + 线段树）
1) 给定 parent 数组 `[-3,1,1,-2,4]`（1-based 解释），执行 `union(2,5)`，写出新的 parent 数组与步骤。答案提示：先找到根并按大小合并。
2) 用线段树构造 `A=[7,2,5,8,3]`，写出 `tree[1]`（根） 的值并演示 `query(2,4)` 的递归过程。
3) 设计一个区间加法的 lazy 线段树并写出 `pushDown` 的核心逻辑（伪代码）。

---
---

## 第9章 图算法（拓扑 / 最短路）
本章详细覆盖：图的表示、拓扑排序、BFS（无权最短路）、Dijkstra（带优先队列）、Bellman-Ford 与 SPFA，含代码模板、手算示例与常见考点。

### A. 图的表示
- 邻接矩阵：适合小/稠密图，空间 O(n^2)，方便判断边是否存在。
- 邻接表：适合稀疏图，空间 O(n+e)，遍历邻边高效（常用于竞赛题/实现）。

常用邻接表初始化（C 风格伪码）：

```text
vector<pair<int,int>> adj[N]; // (to, weight) 或 (to)
addEdge(u,v,w): adj[u].push_back({v,w}); // 有向图
addEdge(u,v,w): adj[u].push_back({v,w}); adj[v].push_back({u,w}); // 无向
```

### B. 拓扑排序（Kahn）

算法要点：先计算入度 indeg[v]，把入度为 0 的节点入队；出队 v，输出 v，并对 v 的每个邻居 w 做 indeg[w]--，若变为 0 则入队。若最终输出顶点数 < |V| 则存在环。

伪代码：

```text
compute indeg[]
queue Q; for v if indeg[v]==0 Q.push(v)
while Q not empty:
  v = Q.pop(); output v
  for (v,w) in adj[v]: indeg[w]--; if indeg[w]==0 Q.push(w)
```

复杂度：O(|V|+|E|)。

常考变式：要求判断唯一拓扑序（每次队列中只有一个元素则唯一），或在给定优先级下生成字典序最小的拓扑序（使用小顶堆替代队列）。

### C. BFS（无权最短路）

使用队列从源点开始层序遍历，记录 `dist[v] = dist[u] + 1`，得到以边数为代价的单源最短路，复杂度 O(|V|+|E|)。

### D. Dijkstra（非负权单源最短路）

核心：使用优先队列（最小堆）存放候选 `(dist, v)`，每次弹出当前最小 `d,u`，若 `d > dist[u]` 则跳过；对 u 的每条边松弛：若 `dist[v] > dist[u] + w` 则更新并 push 新候选。

伪代码：

```text
dist[] = INF; dist[s]=0; PQ.push(0,s)
while PQ not empty:
  d,u = PQ.pop()
  if d>dist[u] continue
  for (u,v,w) in adj[u]:
    if dist[v] > dist[u]+w: dist[v]=dist[u]+w; prev[v]=u; PQ.push(dist[v],v)
```

复杂度（使用二叉堆）：O(|E| log |V|)。常见优化或实现要点：
- 初始化 INF（注意整数溢出），在松弛时检查 `d>dist[u]`。
- 如果需要输出路径，维护 `prev[]`。

示例手算（小图）：
- 图：0->1(w=4),0->2(w=1),2->1(w=2),1->3(w=1),2->3(w=5)
- 初始 dist[0]=0 others INF
- PQ 流程：pop (0,0) 松弛 -> push (1,2),(4,1) ... 继续弹最小候选并更新 dist，最终得到 dist[3]=3（0->2->1->3）。

### E. Bellman-Ford 与 SPFA

Bellman-Ford：对所有边做 |V|-1 次松弛可以求解含负权边的单源最短路并检测负权回路（若再做一次松弛仍能改进则存在负环）。复杂度 O(|V||E|)。

SPFA：基于队列的松弛优化版，平均快但最坏情况仍差；实现时需注意负环检测（计数每个节点入队次数）。

### F. 常见题型与易错点
- 忘记初始化 `dist` 为 INF 或使用不适当的大值造成溢出。 
- 在 Dijkstra 中没有跳过 `d>dist[u]` 的旧条目，导致重复工作但不影响正确性；若误用减小键（decrease-key）接口需正确实现。
- 拓扑排序题注意判断是否存在环以及是否要求唯一。 

### G. 练习题（含思路）
1) 给图（边表）手算拓扑序，并判断是否唯一（提示：每步队列大小判断）。
2) 对上文小图手算 Dijkstra，写出每一步被弹出的 `(dist,vertex)` 及松弛操作结果（答案见上文演示）。
3) 给含负边但无负环的图，手算 Bellman-Ford 的 `dist[]` 更新过程并演示如何检测负环。

---
---

## 常见题型汇总与真题例析（含你提供的题）

快速要点：
- 复杂度题 → 识别循环变换与递推，优先用主定理与倍增法。
- 栈/队列题 → 用栈/队列模拟小规模过程以判断可行性。
- 树题 → 遍历序列转换、重建、删除模拟。
- 堆题 → 熟练数组下标与上/下滤过程。
- 并查集 → 理解数组表示与 union-by-size 更新规则。
- 图题 → 拓扑排序、Dijkstra、BFS 的步骤模拟。

如需，我可以把你提供的往年题逐题写出完整解析并分类存为 `复习/题库/`。

---

## 附录：若干完整示例解析（节选）

### 示例：比较四个算法在 N=200 的运行时间
已知：A: 100 @ O(N)；B:30 @ O(N^2)；C:30 @ O(N^3)；D:10 @ O(N^4)。求 N=200 时最快。
解法：估常数 c，然后算 c·g(200)：
- A: c_A=100/100=1 → 1*200=200
- B: c_B=30/10000=0.003 → 0.003*200^2=120
- C: c_C=30/1e6=3e-5 → 3e-5*8e6=240
- D: c_D=10/1e8=1e-7 → 1e-7*1.6e9=160
最小为 B（120），因此 B 最快。

### 示例：并查集合并步骤（简要）
给出 parent 数组并按 union-by-size 合并两个元素的集合，演示 Find 和更新 parent 的过程（详见练习题答案）。

---

## 后续可选工作
- 按章节拆分题库并写出每题完整解析（每章 8–12 题）。
- 导出为 PDF 或生成打印版模拟试卷。

文件已更新并保存：`复习/复习全章详解.md`。
