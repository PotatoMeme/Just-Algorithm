# 탐색(DFS,BFS) 알고리즘

<br/>

    그래프를 탐색하는 방법에는 크게 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS)이 있습니다.
    여기서 그래프란, 정점(node)과 그 정점을 연결하는 간선(edge)으로 이루어진 자료구조의 일종을 말하며,
    그래프를 탐색한다는 것은 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것을 말합니다.

<br/>

<br/>
<h2><b>깊이 우선 탐색 (DFS, Depth-First Search)</b></h2>
<hr><br/>

루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식을 말함.

<br/>

>  <br/>
>
> - 모든 노드를 방문하고자 하는 경우에 이 방법을 선택
> - 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 좀 더 간단함
> - 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느림
> - 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색
> - 스택 또는 재귀함수로 구현
>
>   <br/>
> <br/>

<h2><b>너비 우선 탐색 (BFS, Breadth-First Search)</b></h2>
<hr><br/>

루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법으로,
시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법을 말함.

<br/>

>  <br/>
>
> - 두 노드 사이의 최단 경로를 찾고 싶을 때 이 방법을 선택
> - 현재 정점에 연결된 가까운 점들부터 탐색
> - 큐를 이용해서 구현
>
>   <br/>

<br/>
<h2><b>문제 유형/응용</b></h2>
<hr><br/>

1. 그래프의 모든 정점을 방문하는 것이 주요한 문제
2. 경로의 특징을 저장해둬야 하는 문제, DFS
3. 최단거리 구해야 하는 문제, BFS

<br/>

- 검색 대상 그래프가 정말 크다면 DFS를 고려
- 검색대상의 규모가 크지 않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않다면 BFS

<br/>
<h3>Example</h3>
<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div><div style="line-height:130%">24</div><div style="line-height:130%">25</div><div style="line-height:130%">26</div><div style="line-height:130%">27</div><div style="line-height:130%">28</div><div style="line-height:130%">29</div><div style="line-height:130%">30</div><div style="line-height:130%">31</div><div style="line-height:130%">32</div><div style="line-height:130%">33</div><div style="line-height:130%">34</div><div style="line-height:130%">35</div><div style="line-height:130%">36</div><div style="line-height:130%">37</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">graph_list&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;{<span style="color:#c10aff">1</span>:&nbsp;set([<span style="color:#c10aff">3</span>,&nbsp;<span style="color:#c10aff">4</span>]),</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#c10aff">2</span>:&nbsp;set([<span style="color:#c10aff">3</span>,&nbsp;<span style="color:#c10aff">4</span>,&nbsp;<span style="color:#c10aff">5</span>]),</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#c10aff">3</span>:&nbsp;set([<span style="color:#c10aff">1</span>,&nbsp;<span style="color:#c10aff">5</span>]),</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#c10aff">4</span>:&nbsp;set([<span style="color:#c10aff">1</span>]),</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#c10aff">5</span>:&nbsp;set([<span style="color:#c10aff">2</span>,&nbsp;<span style="color:#c10aff">6</span>]),</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#c10aff">6</span>:&nbsp;set([<span style="color:#c10aff">3</span>,&nbsp;<span style="color:#c10aff">5</span>])}</div><div style="padding:0 6px; white-space:pre; line-height:130%">root_node&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#999999">#&nbsp;DFS</span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">def</span>&nbsp;DFS_with_adj_list(graph,&nbsp;root):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;visited&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;stack&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;[root]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;stack:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;stack.pop()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;n&nbsp;<span style="color:#ff3399">not</span>&nbsp;<span style="color:#ff3399">in</span>&nbsp;visited:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;visited.append(n)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stack&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;graph[n]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;set(visited)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;visited</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#4be6fa">print</span>(BFS_with_adj_list(graph_list,&nbsp;root_node))</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">from</span>&nbsp;collections&nbsp;<span style="color:#ff3399">import</span>&nbsp;deque</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#999999">#&nbsp;BFS</span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">def</span>&nbsp;BFS_with_adj_list(graph,&nbsp;root):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;visited&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;queue&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;deque([root])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;queue:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;queue.popleft()</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;n&nbsp;<span style="color:#ff3399">not</span>&nbsp;<span style="color:#ff3399">in</span>&nbsp;visited:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;visited.append(n)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;graph[n]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;set(visited)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;visited</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#4be6fa">print</span>(BFS_with_adj_list(graph_list,&nbsp;root_node))</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div><br/>

# 참고

깊이 우선 탐색(DFS) 과 너비 우선 탐색(BFS) :https://devuna.tistory.com/32

DFS, BFS의 설명, 차이점 : https://velog.io/@lucky-korma/DFS-BFS%EC%9D%98-%EC%84%A4%EB%AA%85-%EC%B0%A8%EC%9D%B4%EC%A0%90

파이썬으로 구현하는 BFS와 DFS : https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
