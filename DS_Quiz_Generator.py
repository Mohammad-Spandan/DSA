from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                  TableStyle, PageBreak, HRFlowable, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ── Color palette ──
C_NAVY   = colors.HexColor("#0D1B2A")
C_BLUE   = colors.HexColor("#1565C0")
C_LBLUE  = colors.HexColor("#E3F2FD")
C_RED    = colors.HexColor("#B71C1C")
C_GREY   = colors.HexColor("#F5F5F5")
C_DGREY  = colors.HexColor("#424242")
C_GREEN  = colors.HexColor("#1B5E20")
C_CODE   = colors.HexColor("#F8F9FA")
C_BORDER = colors.HexColor("#BBDEFB")
C_ORANGE = colors.HexColor("#E65100")
C_PURPLE = colors.HexColor("#4A148C")

SEC_COLORS = [
    colors.HexColor("#0D47A1"),  # Array - deep blue
    colors.HexColor("#1B5E20"),  # Stack - deep green
    colors.HexColor("#BF360C"),  # Queue - deep orange
    colors.HexColor("#4A148C"),  # Tree - deep purple
    colors.HexColor("#004D40"),  # Graph - deep teal
]
SEC_LIGHT = [
    colors.HexColor("#E3F2FD"),
    colors.HexColor("#E8F5E9"),
    colors.HexColor("#FBE9E7"),
    colors.HexColor("#F3E5F5"),
    colors.HexColor("#E0F2F1"),
]

def get_styles():
    s = getSampleStyleSheet()
    base = dict(fontName="Helvetica", fontSize=10, leading=14, textColor=C_DGREY)

    styles = {
        'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=28,
                                 textColor=C_NAVY, alignment=TA_CENTER, spaceAfter=6, leading=34),
        'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=13,
                                    textColor=C_BLUE, alignment=TA_CENTER, spaceAfter=4),
        'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=10,
                                textColor=C_DGREY, alignment=TA_CENTER, spaceAfter=2),
        'sec_title': ParagraphStyle('sec_title', fontName='Helvetica-Bold', fontSize=14,
                                     textColor=colors.white, alignment=TA_CENTER, leading=20),
        'level': ParagraphStyle('level', fontName='Helvetica-BoldOblique', fontSize=10,
                                 textColor=C_BLUE, spaceAfter=4, spaceBefore=10),
        'q_num': ParagraphStyle('q_num', fontName='Helvetica-Bold', fontSize=10,
                                 textColor=C_RED, leading=14),
        'q_text': ParagraphStyle('q_text', fontName='Helvetica', fontSize=10,
                                  textColor=C_NAVY, leading=14, spaceAfter=4),
        'code': ParagraphStyle('code', fontName='Courier', fontSize=8.5,
                                textColor=C_NAVY, leading=13, leftIndent=8,
                                backColor=C_CODE, borderPad=4),
        'opt': ParagraphStyle('opt', fontName='Helvetica', fontSize=9.5,
                               textColor=C_DGREY, leading=13, leftIndent=16),
        'normal': ParagraphStyle('normal', **base),
        'center': ParagraphStyle('center', fontName='Helvetica', fontSize=10,
                                  alignment=TA_CENTER, textColor=C_DGREY),
        'footer_note': ParagraphStyle('footer_note', fontName='Helvetica-Oblique', fontSize=8,
                                       textColor=C_DGREY, alignment=TA_CENTER),
    }
    return styles

ST = get_styles()

def code_block(lines):
    """Return a styled code paragraph."""
    txt = '<br/>'.join(lines)
    return Paragraph(f'<font face="Courier" size="8">{txt}</font>',
                     ParagraphStyle('cb', fontName='Courier', fontSize=8, leading=12,
                                    textColor=C_NAVY, backColor=C_CODE,
                                    leftIndent=8, rightIndent=8, borderPad=5,
                                    borderWidth=0.5, borderColor=C_BORDER,
                                    borderRadius=3, spaceAfter=4, spaceBefore=2))

def q_block(n, q_text, code_lines, opts, sec_idx):
    """Build a single question block."""
    items = []
    # Question label + text
    header = Table([[
        Paragraph(f"Q{n}.", ST['q_num']),
        Paragraph(q_text, ST['q_text'])
    ]], colWidths=[0.38*inch, 6.2*inch])
    header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    items.append(header)

    if code_lines:
        items.append(code_block(code_lines))

    # Options in 2 columns
    opt_rows = []
    for i in range(0, len(opts), 2):
        row = []
        for j in range(2):
            if i+j < len(opts):
                letter = chr(65 + i + j)
                row.append(Paragraph(f'<b>{letter})</b>  {opts[i+j]}', ST['opt']))
            else:
                row.append(Paragraph('', ST['opt']))
        opt_rows.append(row)

    opt_table = Table(opt_rows, colWidths=[3.0*inch, 3.58*inch])
    opt_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    items.append(opt_table)
    items.append(Spacer(1, 6))

    wrapper = Table([[items[0] if len(items)==1 else KeepTogether(items)]],
                    colWidths=[6.88*inch])
    return items

# ════════════════════════════════════════════
# ALL 72 QUESTIONS (coding-heavy)
# ════════════════════════════════════════════
QUESTIONS = [
# ── ARRAYS (1–20) ──
# Beginner
(1, 0, "What is the output of this code?",
 ["arr = [10, 20, 30, 40, 50]",
  "print(arr[1], arr[-1], arr[2:4])"],
 ["20 50 [30, 40]", "10 50 [30, 40]", "20 40 [30, 40]", "20 50 [40, 50]"], "A"),

(2, 0, "What does this code print?",
 ["arr = [1, 2, 3, 4, 5]",
  "arr.insert(2, 99)",
  "print(arr)"],
 ["[1, 2, 99, 3, 4, 5]", "[1, 2, 3, 99, 4, 5]", "[99, 1, 2, 3, 4, 5]", "[1, 2, 3, 4, 99, 5]"], "A"),

(3, 0, "What is the time complexity of this function?",
 ["def find(arr, target):",
  "    for i in range(len(arr)):",
  "        if arr[i] == target:",
  "            return i",
  "    return -1"],
 ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "C"),

(4, 0, "What does the following code compute?",
 ["arr = [3, 1, 4, 1, 5, 9, 2, 6]",
  "result = max(arr)",
  "print(result)"],
 ["3", "9", "6", "5"], "B"),

(5, 0, "What is the output?",
 ["a = [1, 2, 3]",
  "b = a",
  "b.append(4)",
  "print(a)"],
 ["[1, 2, 3]", "[1, 2, 3, 4]", "Error", "[4, 1, 2, 3]"], "B"),

# Intermediate
(6, 0, "What is the output of this binary search implementation?",
 ["def bs(arr, t):",
  "    l, r = 0, len(arr)-1",
  "    while l <= r:",
  "        m = (l + r) // 2",
  "        if arr[m] == t: return m",
  "        elif arr[m] < t: l = m + 1",
  "        else: r = m - 1",
  "    return -1",
  "print(bs([1,3,5,7,9,11], 7))"],
 ["2", "3", "4", "-1"], "B"),

(7, 0, "What does this function return for arr = [2, 3, 1, 5, 4]?",
 ["def f(arr):",
  "    res = arr[0]",
  "    for x in arr[1:]:",
  "        if x > res: res = x",
  "    return res"],
 ["2", "4", "5", "3"], "C"),

(8, 0, "What is the output of this two-pointer approach?",
 ["def two_sum(arr, t):",
  "    l, r = 0, len(arr)-1",
  "    while l < r:",
  "        s = arr[l] + arr[r]",
  "        if s == t: return (l, r)",
  "        elif s < t: l += 1",
  "        else: r -= 1",
  "    return None",
  "print(two_sum([1,2,3,4,6], 6))"],
 ["(1, 3)", "(0, 4)", "(2, 3)", "(1, 4)"], "A"),

(9, 0, "What does the following prefix sum code output?",
 ["arr = [2, 4, 1, 3, 5]",
  "prefix = [0] * (len(arr)+1)",
  "for i in range(len(arr)):",
  "    prefix[i+1] = prefix[i] + arr[i]",
  "print(prefix[4] - prefix[1])"],
 ["8", "7", "9", "10"], "A"),

(10, 0, "What is the time and space complexity of merge sort?",
 ["def merge_sort(arr):",
  "    if len(arr) <= 1: return arr",
  "    mid = len(arr) // 2",
  "    L = merge_sort(arr[:mid])",
  "    R = merge_sort(arr[mid:])",
  "    return merge(L, R)"],
 ["O(n^2), O(1)", "O(n log n), O(n)", "O(n log n), O(log n)", "O(n), O(n)"], "B"),

(11, 0, "What does this sliding window code compute?",
 ["def max_sum(arr, k):",
  "    window = sum(arr[:k])",
  "    best = window",
  "    for i in range(k, len(arr)):",
  "        window += arr[i] - arr[i-k]",
  "        best = max(best, window)",
  "    return best",
  "print(max_sum([1,4,2,9,7,3], 3))"],
 ["15", "18", "16", "13"], "B"),

(12, 0, "What does Kadane's algorithm return for this input?",
 ["def kadane(arr):",
  "    max_s = cur = arr[0]",
  "    for x in arr[1:]:",
  "        cur = max(x, cur + x)",
  "        max_s = max(max_s, cur)",
  "    return max_s",
  "print(kadane([-2,1,-3,4,-1,2,1,-5,4]))"],
 ["4", "5", "6", "7"], "C"),

# Advanced
(13, 0, "What does this Dutch National Flag partition output?",
 ["def dnf(arr):",
  "    lo = mid = 0; hi = len(arr)-1",
  "    while mid <= hi:",
  "        if arr[mid]==0: arr[lo],arr[mid]=arr[mid],arr[lo]; lo+=1; mid+=1",
  "        elif arr[mid]==1: mid+=1",
  "        else: arr[mid],arr[hi]=arr[hi],arr[mid]; hi-=1",
  "    return arr",
  "print(dnf([2,0,2,1,1,0]))"],
 ["[0,0,1,1,2,2]", "[2,2,1,1,0,0]", "[0,1,2,0,1,2]", "[1,1,0,0,2,2]"], "A"),

(14, 0, "What is the space complexity of in-place quick sort?",
 ["def quicksort(arr, lo, hi):",
  "    if lo < hi:",
  "        p = partition(arr, lo, hi)",
  "        quicksort(arr, lo, p-1)",
  "        quicksort(arr, p+1, hi)"],
 ["O(1)", "O(log n) average call stack", "O(n)", "O(n log n)"], "B"),

(15, 0, "This function finds the next permutation. What does it return for [1,3,2]?",
 ["def next_perm(a):",
  "    i = len(a)-2",
  "    while i>=0 and a[i]>=a[i+1]: i-=1",
  "    if i>=0:",
  "        j=len(a)-1",
  "        while a[j]<=a[i]: j-=1",
  "        a[i],a[j]=a[j],a[i]",
  "    a[i+1:]=a[i+1:][::-1]",
  "    return a"],
 ["[2,1,3]", "[3,1,2]", "[2,3,1]", "[1,3,2]"], "A"),

(16, 0, "What does this cycle detection in array return?",
 ["def find_dup(nums):",
  "    slow = fast = nums[0]",
  "    while True:",
  "        slow = nums[slow]",
  "        fast = nums[nums[fast]]",
  "        if slow == fast: break",
  "    slow = nums[0]",
  "    while slow != fast:",
  "        slow = nums[slow]",
  "        fast = nums[fast]",
  "    return slow",
  "print(find_dup([1,3,4,2,2]))"],
 ["1", "2", "3", "4"], "B"),

(17, 0, "What is the output of this matrix rotation (90 clockwise)?",
 ["mat = [[1,2,3],[4,5,6],[7,8,9]]",
  "n = len(mat)",
  "for i in range(n):",
  "    for j in range(i+1, n):",
  "        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]",
  "for row in mat: row.reverse()",
  "print(mat[0])"],
 ["[7, 4, 1]", "[1, 4, 7]", "[3, 6, 9]", "[9, 6, 3]"], "A"),

(18, 0, "What does this count inversions code return?",
 ["arr = [3, 1, 2]",
  "count = sum(1 for i in range(len(arr))",
  "            for j in range(i+1,len(arr))",
  "            if arr[i]>arr[j])",
  "print(count)"],
 ["1", "2", "3", "0"], "C"),

(19, 0, "What is the output of this sparse array compression?",
 ["data = {0:5, 3:8, 7:2}",
  "print(data.get(3, 0), data.get(5, 0))"],
 ["8 0", "0 8", "8 8", "Error"], "A"),

(20, 0, "This function solves 'trapping rainwater'. What does it return?",
 ["def trap(h):",
  "    l,r=0,len(h)-1; lm=rm=res=0",
  "    while l<r:",
  "        if h[l]<h[r]:",
  "            if h[l]>=lm: lm=h[l]",
  "            else: res+=lm-h[l]",
  "            l+=1",
  "        else:",
  "            if h[r]>=rm: rm=h[r]",
  "            else: res+=rm-h[r]",
  "            r-=1",
  "    return res",
  "print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))"],
 ["4", "5", "6", "7"], "C"),

# ── STACK (21–35) ──
(21, 1, "What does this stack simulation output?",
 ["stack = []",
  "stack.append(1)",
  "stack.append(2)",
  "stack.append(3)",
  "stack.pop()",
  "stack.append(4)",
  "print(stack)"],
 ["[1, 2, 3, 4]", "[1, 2, 4]", "[4, 2, 1]", "[1, 4, 2]"], "B"),

(22, 1, "What does this balanced brackets checker return for '({[]})'?",
 ["def is_balanced(s):",
  "    st = []; m = {')':'(',']':'[','}':'{'}",
  "    for c in s:",
  "        if c in '([{': st.append(c)",
  "        elif not st or st[-1]!=m[c]: return False",
  "        else: st.pop()",
  "    return not st",
  "print(is_balanced('({[]})'))"],
 ["True", "False", "None", "Error"], "A"),

(23, 1, "What is the output of this postfix evaluator?",
 ["def eval_postfix(expr):",
  "    st = []",
  "    for t in expr.split():",
  "        if t.lstrip('-').isdigit(): st.append(int(t))",
  "        else:",
  "            b,a=st.pop(),st.pop()",
  "            st.append(eval(f'{a}{t}{b}'))",
  "    return st[0]",
  "print(eval_postfix('3 4 + 2 * 7 /'))"],
 ["2", "1", "5", "4"], "B"),

(24, 1, "What does this min-stack return?",
 ["class MinStack:",
  "    def push(self,x):",
  "        self.s.append(x)",
  "        m=x if not self.ms else min(x,self.ms[-1])",
  "        self.ms.append(m)",
  "    def get_min(self): return self.ms[-1]",
  "ms=MinStack()",
  "for v in [5,3,7,2,8]: ms.push(v)",
  "print(ms.get_min())"],
 ["5", "3", "2", "8"], "C"),

(25, 1, "What does this code compute using a stack?",
 ["def next_greater(arr):",
  "    res=[-1]*len(arr); st=[]",
  "    for i,v in enumerate(arr):",
  "        while st and arr[st[-1]]<v:",
  "            res[st.pop()]=v",
  "        st.append(i)",
  "    return res",
  "print(next_greater([4,5,2,25]))"],
 ["[5, 25, 25, -1]", "[5, -1, 25, -1]", "[25, 25, 25, -1]", "[-1, 5, 25, -1]"], "A"),

(26, 1, "What does this recursive stack reversal return?",
 ["def insert_bottom(s, item):",
  "    if not s: s.append(item); return",
  "    t=s.pop(); insert_bottom(s,item); s.append(t)",
  "def reverse(s):",
  "    if s:",
  "        t=s.pop(); reverse(s); insert_bottom(s,t)",
  "s=[1,2,3,4]",
  "reverse(s); print(s)"],
 ["[4, 3, 2, 1]", "[1, 2, 3, 4]", "[2, 1, 4, 3]", "Error"], "A"),

(27, 1, "This evaluates an infix expression. What does it return for '3+5*2'?",
 ["def calc(s):",
  "    vals,ops=[],[]",
  "    prec={'+':1,'-':1,'*':2,'/':2}",
  "    def apply():",
  "        b,a=vals.pop(),vals.pop()",
  "        vals.append(int(eval(f'{a}{ops.pop()}{b}')))",
  "    for c in s:",
  "        if c.isdigit(): vals.append(int(c))",
  "        elif c in prec:",
  "            while ops and prec.get(ops[-1],0)>=prec[c]: apply()",
  "            ops.append(c)",
  "    while ops: apply()",
  "    return vals[0]"],
 ["16", "13", "11", "8"], "B"),

(28, 1, "What is the space complexity of DFS on a graph of V vertices?",
 ["def dfs(graph, start):",
  "    visited = set()",
  "    stack = [start]",
  "    while stack:",
  "        node = stack.pop()",
  "        if node not in visited:",
  "            visited.add(node)",
  "            for nb in graph[node]:",
  "                stack.append(nb)",
  "    return visited"],
 ["O(1)", "O(V)", "O(V + E)", "O(E)"], "B"),

(29, 1, "What does this stock span calculator return for [100, 80, 60, 70, 60, 75, 85]?",
 ["def stock_span(prices):",
  "    spans=[]; st=[]",
  "    for i,p in enumerate(prices):",
  "        while st and prices[st[-1]]<=p: st.pop()",
  "        spans.append(i-st[-1] if st else i+1)",
  "        st.append(i)",
  "    return spans"],
 ["[1,1,1,2,1,4,6]", "[1,1,1,2,1,3,5]", "[1,1,1,2,1,4,5]", "[1,1,1,3,1,4,6]"], "A"),

(30, 1, "What is the time complexity of largest rectangle in histogram?",
 ["def largest_rect(heights):",
  "    st=[]; max_area=0",
  "    heights.append(0)",
  "    for i,h in enumerate(heights):",
  "        while st and heights[st[-1]]>h:",
  "            ht=heights[st.pop()]",
  "            w=i if not st else i-st[-1]-1",
  "            max_area=max(max_area,ht*w)",
  "        st.append(i)",
  "    return max_area"],
 ["O(n^2)", "O(n log n)", "O(n)", "O(log n)"], "C"),

(31, 1, "What does this queue using 2-stacks return?",
 ["class Queue:",
  "    def __init__(self): self.s1=[];self.s2=[]",
  "    def enq(self,x): self.s1.append(x)",
  "    def deq(self):",
  "        if not self.s2:",
  "            while self.s1: self.s2.append(self.s1.pop())",
  "        return self.s2.pop()",
  "q=Queue()",
  "for x in [1,2,3]: q.enq(x)",
  "print(q.deq(), q.deq())"],
 ["3 2", "1 2", "2 1", "3 1"], "B"),

(32, 1, "What does the decode string '3[a2[b]]' decode to?",
 ["def decode(s):",
  "    st=[]; cur=''; k=0",
  "    for c in s:",
  "        if c.isdigit(): k=k*10+int(c)",
  "        elif c=='[': st.append((cur,k)); cur=''; k=0",
  "        elif c==']':",
  "            prev,n=st.pop(); cur=prev+n*cur",
  "        else: cur+=c",
  "    return cur"],
 ["aaabbb", "abbbabbbabbb", "abbabb", "ababab"], "B"),

(33, 1, "This removes k digits to get smallest. For num='1432219', k=3 it returns:",
 ["def remove_k(num, k):",
  "    st=[]",
  "    for d in num:",
  "        while k and st and st[-1]>d:",
  "            st.pop(); k-=1",
  "        st.append(d)",
  "    while k: st.pop(); k-=1",
  "    return ''.join(st).lstrip('0') or '0'"],
 ["\"1219\"", "\"1239\"", "\"1223\"", "\"1229\""], "A"),

(34, 1, "What does this asteroid collision simulation return?",
 ["def asteroids(a):",
  "    st=[]",
  "    for x in a:",
  "        alive=True",
  "        while alive and x<0 and st and st[-1]>0:",
  "            if st[-1]<-x: st.pop()",
  "            elif st[-1]==-x: st.pop(); alive=False",
  "            else: alive=False",
  "        if alive: st.append(x)",
  "    return st",
  "print(asteroids([5,10,-5]))"],
 ["[5, 10]", "[10]", "[5]", "[]"], "A"),

(35, 1, "What is the output of this daily temperatures code?",
 ["def wait_days(T):",
  "    res=[0]*len(T); st=[]",
  "    for i,t in enumerate(T):",
  "        while st and T[st[-1]]<t:",
  "            j=st.pop(); res[j]=i-j",
  "        st.append(i)",
  "    return res",
  "print(wait_days([73,74,75,71,69,72,76,73]))"],
 ["[1,1,4,2,1,1,0,0]", "[1,1,1,2,1,1,0,0]", "[1,1,5,2,1,1,0,0]", "[1,1,4,2,1,2,0,0]"], "A"),

# ── QUEUE (36–48) ──
(36, 2, "What does this queue using deque print?",
 ["from collections import deque",
  "q = deque()",
  "q.append(1); q.append(2); q.append(3)",
  "q.popleft()",
  "q.appendleft(0)",
  "print(list(q))"],
 ["[0, 2, 3]", "[0, 1, 2]", "[2, 3, 0]", "[1, 2, 3]"], "A"),

(37, 2, "What does this circular queue check return?",
 ["class CQ:",
  "    def __init__(self,k): self.q=[None]*k;self.h=self.t=self.sz=0;self.k=k",
  "    def enq(self,v):",
  "        if self.sz==self.k: return False",
  "        self.q[self.t]=v;self.t=(self.t+1)%self.k;self.sz+=1;return True",
  "    def deq(self):",
  "        if not self.sz: return -1",
  "        v=self.q[self.h];self.h=(self.h+1)%self.k;self.sz-=1;return v",
  "cq=CQ(3)",
  "cq.enq(1);cq.enq(2);cq.enq(3)",
  "print(cq.enq(4), cq.deq(), cq.enq(4))"],
 ["False 1 True", "True 1 True", "False 2 False", "True 2 True"], "A"),

(38, 2, "What does this BFS level-order traversal return?",
 ["from collections import deque",
  "def bfs(root, adj):",
  "    q=deque([root]); levels=[]",
  "    while q:",
  "        lvl=[]",
  "        for _ in range(len(q)):",
  "            n=q.popleft(); lvl.append(n)",
  "            for c in adj.get(n,[]): q.append(c)",
  "        levels.append(lvl)",
  "    return levels"],
 ["[[1],[2,3],[4,5]]", "[[1],[3,2],[5,4]]", "[[1,2,3],[4,5]]", "[[1],[2],[3],[4],[5]]"], "A"),

(39, 2, "What is the output of this sliding window maximum?",
 ["from collections import deque",
  "def sw_max(arr, k):",
  "    dq=deque(); res=[]",
  "    for i,v in enumerate(arr):",
  "        while dq and dq[0]<i-k+1: dq.popleft()",
  "        while dq and arr[dq[-1]]<v: dq.pop()",
  "        dq.append(i)",
  "        if i>=k-1: res.append(arr[dq[0]])",
  "    return res",
  "print(sw_max([1,3,-1,-3,5,3,6,7],3))"],
 ["[3,3,5,5,6,7]", "[3,3,3,5,6,7]", "[3,-1,-3,5,3,7]", "[1,3,5,6,7]"], "A"),

(40, 2, "What does this priority queue (min-heap) print?",
 ["import heapq",
  "pq = [5, 3, 8, 1, 2]",
  "heapq.heapify(pq)",
  "heapq.heappush(pq, 0)",
  "print(heapq.heappop(pq), heapq.heappop(pq))"],
 ["5 3", "0 1", "1 2", "3 5"], "B"),

(41, 2, "What does this BFS shortest path return?",
 ["from collections import deque",
  "def bfs_path(g, s, t):",
  "    q=deque([[s]]); seen={s}",
  "    while q:",
  "        path=q.popleft()",
  "        if path[-1]==t: return len(path)-1",
  "        for nb in g[path[-1]]:",
  "            if nb not in seen:",
  "                seen.add(nb); q.append(path+[nb])",
  "    return -1",
  "g={0:[1,2],1:[3],2:[3],3:[4],4:[]}",
  "print(bfs_path(g,0,4))"],
 ["2", "3", "4", "1"], "B"),

(42, 2, "What does this task scheduler return for tasks=['A','A','A','B','B','B'], n=2?",
 ["from collections import Counter",
  "def scheduler(tasks, n):",
  "    freq=sorted(Counter(tasks).values())",
  "    max_f=freq[-1]; max_cnt=freq.count(max_f)",
  "    return max(len(tasks),(max_f-1)*(n+1)+max_cnt)",
  "print(scheduler(['A','A','A','B','B','B'],2))"],
 ["6", "7", "8", "9"], "C"),

(43, 2, "What does this k-th largest element return?",
 ["import heapq",
  "def kth_largest(nums, k):",
  "    heap = nums[:k]",
  "    heapq.heapify(heap)",
  "    for n in nums[k:]:",
  "        if n > heap[0]:",
  "            heapq.heapreplace(heap, n)",
  "    return heap[0]",
  "print(kth_largest([3,2,1,5,6,4], 2))"],
 ["4", "5", "6", "3"], "B"),

(44, 2, "What is the time complexity of Dijkstra with min-heap?",
 ["import heapq",
  "def dijkstra(graph, src):",
  "    dist={src:0}; pq=[(0,src)]",
  "    while pq:",
  "        d,u=heapq.heappop(pq)",
  "        for v,w in graph[u]:",
  "            if d+w < dist.get(v,float('inf')):",
  "                dist[v]=d+w",
  "                heapq.heappush(pq,(dist[v],v))",
  "    return dist"],
 ["O(V^2)", "O(E log V)", "O(V log V)", "O(VE)"], "B"),

(45, 2, "What does this LRU Cache return?",
 ["from collections import OrderedDict",
  "class LRU:",
  "    def __init__(self,cap): self.c=cap;self.d=OrderedDict()",
  "    def get(self,k): ",
  "        if k not in self.d: return -1",
  "        self.d.move_to_end(k); return self.d[k]",
  "    def put(self,k,v):",
  "        if k in self.d: self.d.move_to_end(k)",
  "        self.d[k]=v",
  "        if len(self.d)>self.c: self.d.popitem(last=False)",
  "lru=LRU(2)",
  "lru.put(1,1);lru.put(2,2);lru.get(1);lru.put(3,3)",
  "print(lru.get(2))"],
 ["2", "1", "-1", "3"], "C"),

(46, 2, "What does this BFS island counter return?",
 ["from collections import deque",
  "def count_islands(grid):",
  "    count=0",
  "    for r in range(len(grid)):",
  "        for c in range(len(grid[0])):",
  "            if grid[r][c]=='1':",
  "                count+=1; q=deque([(r,c)]); grid[r][c]='0'",
  "                while q:",
  "                    x,y=q.popleft()",
  "                    for dx,dy in[(1,0),(-1,0),(0,1),(0,-1)]:",
  "                        if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]=='1':",
  "                            q.append((x+dx,y+dy));grid[x+dx][y+dy]='0'",
  "    return count",
  "g=[['1','1','0'],['0','1','0'],['0','0','1']]",
  "print(count_islands(g))"],
 ["1", "2", "3", "4"], "B"),

(47, 2, "What does this median finder return after adding [5,3,8,4]?",
 ["import heapq",
  "class MedianFinder:",
  "    def __init__(self): self.lo=[];self.hi=[]",
  "    def add(self,n):",
  "        heapq.heappush(self.lo,-n)",
  "        heapq.heappush(self.hi,-heapq.heappop(self.lo))",
  "        if len(self.hi)>len(self.lo):",
  "            heapq.heappush(self.lo,-heapq.heappop(self.hi))",
  "    def median(self):",
  "        if len(self.lo)>len(self.hi): return -self.lo[0]",
  "        return (-self.lo[0]+self.hi[0])/2",
  "mf=MedianFinder()",
  "for x in [5,3,8,4]: mf.add(x)",
  "print(mf.median())"],
 ["4.5", "5.0", "4.0", "5.5"], "A"),

(48, 2, "What does this topological sort return for edges [(0,1),(0,2),(1,3),(2,3)]?",
 ["from collections import deque",
  "def topo(n, edges):",
  "    ind=[0]*n; adj=[[] for _ in range(n)]",
  "    for u,v in edges: adj[u].append(v);ind[v]+=1",
  "    q=deque([i for i in range(n) if ind[i]==0])",
  "    order=[]",
  "    while q:",
  "        u=q.popleft(); order.append(u)",
  "        for v in adj[u]:",
  "            ind[v]-=1",
  "            if ind[v]==0: q.append(v)",
  "    return order",
  "print(topo(4,[(0,1),(0,2),(1,3),(2,3)]))"],
 ["[0,1,2,3]", "[0,2,1,3]", "Both A and B are valid", "[3,1,2,0]"], "C"),

# ── TREE (49–60) ──
(49, 3, "What does this BST insertion and in-order traversal return?",
 ["class Node:",
  "    def __init__(self,v): self.v=v;self.l=self.r=None",
  "def insert(root,v):",
  "    if not root: return Node(v)",
  "    if v<root.v: root.l=insert(root.l,v)",
  "    else: root.r=insert(root.r,v)",
  "    return root",
  "r=None",
  "for v in [5,3,7,1,4]: r=insert(r,v)",
  "def inorder(root,res=[]):",
  "    if root: inorder(root.l,res);res.append(root.v);inorder(root.r,res)",
  "    return res",
  "print(inorder(r,[]))"],
 ["[1,3,4,5,7]", "[5,3,7,1,4]", "[1,4,3,7,5]", "[5,7,3,4,1]"], "A"),

(50, 3, "What does this BST search return for key=4?",
 ["def search(root, k):",
  "    if not root or root.v==k: return root",
  "    if k < root.v: return search(root.l, k)",
  "    return search(root.r, k)"],
 ["False", "True", "None", "Error"], "B"),

(51, 3, "What is the height of a balanced BST from [1,2,3,4,5,6,7]?",
 ["def height(root):",
  "    if not root: return -1",
  "    return 1 + max(height(root.l), height(root.r))"],
 ["2", "3", "4", "7"], "A"),

(52, 3, "What does this level-order traversal return?",
 ["from collections import deque",
  "def level_order(root):",
  "    if not root: return []",
  "    q=deque([root]); res=[]",
  "    while q:",
  "        node=q.popleft(); res.append(node.v)",
  "        if node.l: q.append(node.l)",
  "        if node.r: q.append(node.r)",
  "    return res"],
 ["[1,2,3,4,5]", "[4,2,5,1,3]", "[1,3,2,5,4]", "[4,5,2,3,1]"], "A"),

(53, 3, "What does this LCA function return for nodes 4 and 5?",
 ["def lca(root, p, q):",
  "    while root:",
  "        if p < root.v and q < root.v: root=root.l",
  "        elif p > root.v and q > root.v: root=root.r",
  "        else: return root.v"],
 ["2", "4", "6", "3"], "B"),

(54, 3, "What is the time complexity of AVL rotation?",
 ["def right_rotate(y):",
  "    x=y.left; T2=x.right",
  "    x.right=y; y.left=T2",
  "    y.height=1+max(get_h(y.left),get_h(y.right))",
  "    x.height=1+max(get_h(x.left),get_h(x.right))",
  "    return x"],
 ["O(n)", "O(log n)", "O(1)", "O(n log n)"], "C"),

(55, 3, "What does this valid BST checker return?",
 ["def is_bst(root, mn=float('-inf'), mx=float('inf')):",
  "    if not root: return True",
  "    if root.v<=mn or root.v>=mx: return False",
  "    return (is_bst(root.l, mn, root.v) and",
  "            is_bst(root.r, root.v, mx))"],
 ["True", "False", "None", "Error"], "B"),

(56, 3, "What does this heap push/pop sequence return?",
 ["import heapq",
  "h=[]",
  "for v in [3,1,4,1,5,9,2,6]: heapq.heappush(h,v)",
  "result=[]",
  "while h: result.append(heapq.heappop(h))",
  "print(result[:4])"],
 ["[1,1,2,3]", "[1,2,3,4]", "[3,1,4,1]", "[9,6,5,4]"], "A"),

(57, 3, "What does this segment tree range sum query return?",
 ["def build(arr,tree,i,l,r):",
  "    if l==r: tree[i]=arr[l]; return",
  "    m=(l+r)//2",
  "    build(arr,tree,2*i,l,m)",
  "    build(arr,tree,2*i+1,m+1,r)",
  "    tree[i]=tree[2*i]+tree[2*i+1]",
  "arr=[1,3,5,7,9,11]",
  "tree=[0]*24; build(arr,tree,1,0,5)",
  "# Sum of indices 1-3 (values 3,5,7)"],
 ["10", "15", "18", "8"], "B"),

(58, 3, "What does this trie insert + search return?",
 ["class Trie:",
  "    def __init__(self): self.c={}; self.end=False",
  "    def insert(self,w):",
  "        n=self",
  "        for ch in w:",
  "            if ch not in n.c: n.c[ch]=Trie()",
  "            n=n.c[ch]",
  "        n.end=True",
  "    def search(self,w):",
  "        n=self",
  "        for ch in w:",
  "            if ch not in n.c: return False",
  "            n=n.c[ch]",
  "        return n.end",
  "t=Trie(); t.insert('apple')",
  "print(t.search('apple'), t.search('app'))"],
 ["True True", "True False", "False True", "False False"], "B"),

(59, 3, "What does this Morris in-order traversal return?",
 ["def morris_inorder(root):",
  "    res=[]; cur=root",
  "    while cur:",
  "        if not cur.l: res.append(cur.v); cur=cur.r",
  "        else:",
  "            pre=cur.l",
  "            while pre.r and pre.r!=cur: pre=pre.r",
  "            if not pre.r: pre.r=cur; cur=cur.l",
  "            else: pre.r=None; res.append(cur.v); cur=cur.r",
  "    return res"],
 ["[1,3,4,5,7]", "[5,3,7,1,4]", "[1,4,3,7,5]", "[5,7,3,4,1]"], "A"),

(60, 3, "What is the time complexity of building a Fenwick tree?",
 ["def build_fenwick(arr):",
  "    n=len(arr); bit=[0]*(n+1)",
  "    for i,v in enumerate(arr,1):",
  "        bit[i]+=v",
  "        j=i+(i&-i)",
  "        if j<=n: bit[j]+=bit[i]",
  "    return bit"],
 ["O(n^2)", "O(n log n)", "O(n)", "O(log n)"], "C"),

# ── GRAPH (61–72) ──
(61, 4, "What does this DFS return for graph {0:[1,2],1:[3],2:[3],3:[]}?",
 ["def dfs(g, node, visited=None):",
  "    if visited is None: visited=[]",
  "    visited.append(node)",
  "    for nb in g.get(node,[]):",
  "        if nb not in visited: dfs(g,nb,visited)",
  "    return visited",
  "print(dfs({0:[1,2],1:[3],2:[3],3:[]}, 0))"],
 ["[0,1,2,3]", "[0,1,3,2]", "[0,2,1,3]", "[3,1,2,0]"], "B"),

(62, 4, "What is the space complexity for an adjacency list with V vertices and E edges?",
 ["graph = {",
  "    0: [1, 2],",
  "    1: [0, 3],",
  "    2: [0, 3],",
  "    3: [1, 2]",
  "}"],
 ["O(V)", "O(E)", "O(V + E)", "O(V * E)"], "C"),

(63, 4, "What does this cycle detection return for edges [(0,1),(1,2),(2,0)]?",
 ["def has_cycle(n, edges):",
  "    adj=[[] for _ in range(n)]",
  "    for u,v in edges: adj[u].append(v)",
  "    color=[0]*n",
  "    def dfs(u):",
  "        color[u]=1",
  "        for v in adj[u]:",
  "            if color[v]==1: return True",
  "            if color[v]==0 and dfs(v): return True",
  "        color[u]=2; return False",
  "    return any(dfs(i) for i in range(n) if color[i]==0)"],
 ["False", "True", "None", "Error"], "B"),

(64, 4, "What does Dijkstra return as distance from 0 to 4?",
 ["import heapq",
  "g = {0:[(1,4),(2,1)], 1:[(3,1)], 2:[(1,2),(3,5)], 3:[(4,3)], 4:[]}",
  "def dijkstra(g,s):",
  "    dist={s:0}; pq=[(0,s)]",
  "    while pq:",
  "        d,u=heapq.heappop(pq)",
  "        for v,w in g[u]:",
  "            if d+w<dist.get(v,float('inf')):",
  "                dist[v]=d+w; heapq.heappush(pq,(dist[v],v))",
  "    return dist"],
 ["7", "8", "9", "6"], "B"),

(65, 4, "What does Bellman-Ford return for edges with negative cycle?",
 ["def bellman_ford(n, edges, src):",
  "    dist=[float('inf')]*n; dist[src]=0",
  "    for _ in range(n-1):",
  "        for u,v,w in edges:",
  "            if dist[u]+w<dist[v]: dist[v]=dist[u]+w",
  "    for u,v,w in edges:",
  "        if dist[u]+w<dist[v]: return True",
  "    return False"],
 ["False", "True", "None", "0"], "B"),

(66, 4, "What does this Union-Find return after unions?",
 ["class DSU:",
  "    def __init__(self,n): self.p=list(range(n));self.r=[0]*n",
  "    def find(self,x):",
  "        if self.p[x]!=x: self.p[x]=self.find(self.p[x])",
  "        return self.p[x]",
  "    def union(self,x,y):",
  "        px,py=self.find(x),self.find(y)",
  "        if px==py: return False",
  "        if self.r[px]<self.r[py]: px,py=py,px",
  "        self.p[py]=px",
  "        if self.r[px]==self.r[py]: self.r[px]+=1",
  "        return True",
  "d=DSU(5)",
  "d.union(0,1);d.union(1,2);d.union(3,4)",
  "print(d.find(0)==d.find(2), d.find(0)==d.find(3))"],
 ["True True", "True False", "False True", "False False"], "B"),

(67, 4, "What does Kruskal's MST return as total weight?",
 ["def kruskal(n, edges):",
  "    edges.sort(key=lambda x:x[2])",
  "    dsu=DSU(n); total=0; cnt=0",
  "    for u,v,w in edges:",
  "        if dsu.union(u,v):",
  "            total+=w; cnt+=1",
  "            if cnt==n-1: break",
  "    return total"],
 ["4", "5", "6", "7"], "A"),

(68, 4, "What does this bipartite check return for cycle graph 0-1-2-3-0?",
 ["from collections import deque",
  "def is_bipartite(graph, n):",
  "    color=[-1]*n",
  "    for s in range(n):",
  "        if color[s]!=-1: continue",
  "        q=deque([s]); color[s]=0",
  "        while q:",
  "            u=q.popleft()",
  "            for v in graph[u]:",
  "                if color[v]==-1: color[v]=1-color[u]; q.append(v)",
  "                elif color[v]==color[u]: return False",
  "    return True"],
 ["False", "True", "None", "Error"], "B"),

(69, 4, "What does Floyd-Warshall return for shortest path from 0 to 3?",
 ["INF=float('inf')",
  "dist=[[0,3,INF,7],[8,0,2,INF],[5,INF,0,1],[2,INF,INF,0]]",
  "n=4",
  "for k in range(n):",
  "    for i in range(n):",
  "        for j in range(n):",
  "            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])",
  "print(dist[0][3])"],
 ["7", "6", "5", "4"], "B"),

(70, 4, "What does Prim's MST implementation return as total weight?",
 ["import heapq",
  "def prim(graph, n):",
  "    visited=set([0]); edges=graph[0][:]",
  "    heapq.heapify(edges); total=0",
  "    while edges and len(visited)<n:",
  "        w,u,v=heapq.heappop(edges)",
  "        if v not in visited:",
  "            visited.add(v); total+=w",
  "            for edge in graph[v]: heapq.heappush(edges,edge)",
  "    return total"],
 ["5", "6", "7", "8"], "C"),

(71, 4, "What does topological DFS-based sort return?",
 ["def topo_dfs(n, adj):",
  "    visited=set(); stack=[]",
  "    def dfs(u):",
  "        visited.add(u)",
  "        for v in adj.get(u,[]): ",
  "            if v not in visited: dfs(v)",
  "        stack.append(u)",
  "    for i in range(n):",
  "        if i not in visited: dfs(i)",
  "    return stack[::-1]"],
 ["[5,4,2,3,1,0]", "[0,1,3,2,4,5]", "[4,5,0,2,3,1]", "Multiple valid answers exist"], "D"),

(72, 4, "What is the time complexity of Tarjan's SCC algorithm?",
 ["def tarjan(graph, n):",
  "    disc=[-1]*n; low=[-1]*n; on_stack=[False]*n",
  "    stack=[]; timer=[0]; sccs=[]",
  "    def dfs(u):",
  "        disc[u]=low[u]=timer[0]; timer[0]+=1",
  "        stack.append(u); on_stack[u]=True",
  "        for v in graph[u]:",
  "            if disc[v]==-1: dfs(v); low[u]=min(low[u],low[v])",
  "            elif on_stack[v]: low[u]=min(low[u],disc[v])",
  "        if low[u]==disc[u]:",
  "            scc=[]",
  "            while True:",
  "                w=stack.pop(); on_stack[w]=False; scc.append(w)",
  "                if w==u: break",
  "            sccs.append(scc)",
  "    for i in range(n):",
  "        if disc[i]==-1: dfs(i)",
  "    return sccs"],
 ["O(V^2)", "O(V + E)", "O(E log V)", "O(VE)"], "B"),
]

def make_section_header(title, color, light_color):
    table = Table([[Paragraph(title, ST['sec_title'])]],
                  colWidths=[7.0*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('ROUNDEDCORNERS', [4,4,4,4]),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
    ]))
    return table

def build_quiz():
    doc = SimpleDocTemplate("DS_Quiz_Coding.pdf", pagesize=letter,
                             leftMargin=0.65*inch, rightMargin=0.65*inch,
                             topMargin=0.65*inch, bottomMargin=0.65*inch)
    story = []

    # ── Cover page ──
    story.append(Spacer(1, 0.6*inch))
    # Big header bar
    cover_bar = Table([[Paragraph("DATA STRUCTURES", ParagraphStyle(
        'ct', fontName='Helvetica-Bold', fontSize=32, textColor=colors.white, alignment=TA_CENTER))]],
        colWidths=[7.0*inch])
    cover_bar.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_NAVY),
        ('TOPPADDING', (0,0), (-1,-1), 18), ('BOTTOMPADDING', (0,0), (-1,-1), 18),
    ]))
    story.append(cover_bar)
    story.append(Spacer(1, 0.12*inch))

    sub_bar = Table([[Paragraph("CODING QUIZ PAPER", ParagraphStyle(
        'cs', fontName='Helvetica-Bold', fontSize=18, textColor=colors.white, alignment=TA_CENTER))]],
        colWidths=[7.0*inch])
    sub_bar.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 10), ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(sub_bar)
    story.append(Spacer(1, 0.3*inch))

    # Info grid
    info = Table([
        [Paragraph("<b>72 Output / Tracing / Complexity Questions</b>", ST['normal']),
         Paragraph("<b>Topics:</b> Array · Stack · Queue · Tree · Graph", ST['normal'])],
        [Paragraph("<b>Level:</b>  Beginner → Intermediate → Advanced", ST['normal']),
         Paragraph("<b>Language:</b>  Python 3", ST['normal'])],
    ], colWidths=[3.5*inch, 3.5*inch])
    info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LBLUE),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(info)
    story.append(Spacer(1, 0.4*inch))

    # Name / date / score
    fields = Table([
        [Paragraph("Name:", ST['normal']), Paragraph("_" * 38, ST['normal']),
         Paragraph("Date:", ST['normal']), Paragraph("_" * 18, ST['normal'])],
        [Paragraph("Score:", ST['normal']), Paragraph("_____ / 72", ST['normal']),
         Paragraph("Time:", ST['normal']), Paragraph("_______  mins", ST['normal'])],
    ], colWidths=[0.7*inch, 3.2*inch, 0.7*inch, 2.4*inch])
    fields.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(fields)
    story.append(Spacer(1, 0.3*inch))
    story.append(HRFlowable(width="100%", thickness=1, color=C_BLUE))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "<i>Instructions: Read each code snippet carefully and circle the correct answer. "
        "Each question is worth 1 mark. No partial credit.</i>", ST['footer_note']))

    story.append(PageBreak())

    # ── Questions ──
    q_map = {q[0]: q for q in QUESTIONS}
    
    sec_ranges = [
        (range(1, 21), 0, [1,6,13], "◆  SECTION 1: ARRAYS  —  Questions 1–20"),
        (range(21, 36), 1, [21,26,31], "◆  SECTION 2: STACK  —  Questions 21–35"),
        (range(36, 49), 2, [36,41,47], "◆  SECTION 3: QUEUE  —  Questions 36–48"),
        (range(49, 61), 3, [49,54,58], "◆  SECTION 4: TREE  —  Questions 49–60"),
        (range(61, 73), 4, [61,64,68], "◆  SECTION 5: GRAPH  —  Questions 61–72"),
    ]

    for sec_range, s_idx, level_starts, sec_title in sec_ranges:
        story.append(make_section_header(sec_title, SEC_COLORS[s_idx], SEC_LIGHT[s_idx]))
        story.append(Spacer(1, 0.1*inch))

        for qn in sec_range:
            if qn in q_map:
                q = q_map[qn]
                if qn in level_starts:
                    level_map = {level_starts[0]:"🟢  Beginner Level",
                                level_starts[1]:"🟡  Intermediate Level",
                                level_starts[2]:"🔴  Advanced Level"}
                    lbl = level_map.get(qn, "")
                    story.append(Spacer(1, 4))
                    story.append(Paragraph(lbl, ST['level']))

                items = q_block(qn, q[2], q[3], q[4], q[1])
                story.append(KeepTogether(items))

        story.append(PageBreak())

    story.append(Paragraph("— END OF QUIZ PAPER —", ST['center']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Answer Key is on the separate Solution Paper.", ST['footer_note']))

    doc.build(story)
    print("✓ Quiz PDF generated: DS_Quiz_Coding.pdf")

if __name__ == "__main__":
    build_quiz()
