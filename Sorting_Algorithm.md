# 정렬 알고리즘

<br/>

    정렬 알고리즘, n개의 숫자가 입력으로 주어졌을때 이를 문제의 기준과 맞게 정렬하여 출력하는 알고리즘

    이러한 정렬알고리즘 문제같은경우 선택 정렬, 삽입 정렬, 버블 정렬, 합병 정렬, 퀵 정렬등으로 나눌수 있습니다.

<br/>

---

<br/>
<h2><b>선택 정렬의 경우</b></h2>
<hr><br/>
    
선택 정렬은 현재 위치에 들어갈 값을 찾아 정렬하는 방법이다. 현재 위치에 저장 될 값의 크기가 작냐, 크냐에 따라 최소 선택 정렬(Min-Selection Sort)과 최대 선택 정렬(Max-Selection Sort)로 구분

<br/>

> ## 로직
>
> - 정렬 되지 않은 인덱스의 맨 앞에서 부터, 이를 포함한 그 이후의 배열값 중 가장 작은 값을 찾아간다.
> - 가장 작은 값을 찾으면, 그 값을 현재 인덱스의 값과 바꿔준다.
> - 다음 인덱스에서 위 과정을 반복해준다.
>   <br/><br/>
>   시간복잡도 : O(n^2) <br/>
>   공간복잡도 : O(n)

<br/>
<h3>Example</h3>
<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">array&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;list({<span style="color:#c10aff">8</span>,&nbsp;<span style="color:#c10aff">7</span>,&nbsp;<span style="color:#c10aff">6</span>,&nbsp;<span style="color:#c10aff">5</span>,&nbsp;<span style="color:#c10aff">4</span>,&nbsp;<span style="color:#c10aff">3</span>,&nbsp;<span style="color:#c10aff">1</span>,&nbsp;<span style="color:#c10aff">4</span>})</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">for</span>&nbsp;i&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(<span style="color:#4be6fa">len</span>(array)<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span>):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;temp&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;i</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">for</span>&nbsp;j&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(i<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>,&nbsp;<span style="color:#4be6fa">len</span>(array)):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;array[temp]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;array[j]:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;j</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;array[i],&nbsp;array[temp]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;array[temp],&nbsp;array[i]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>
<br>

| 장점                                      | 단점                   |
| :---------------------------------------- | ---------------------- |
| 구현이 간단하다                           | 정렬 시간이 오래걸린다 |
| 비교하는 횟수에 비해 교환이 적게 일어난다 |                        |

---

<br/>
<h2><b>삽입 정렬의 경우</b></h2>
<hr><br/>

삽입 정렬은 현재 위치에서, 그 이하의 배열들을 비교하여 자신이 들어갈 위치를 찾아, 그 위치에 삽입하는 방법이다.

<br/>

> ## 로직
>
> - 삽입 정렬은 두 번째 인덱스부터 시작한다. 현재 인덱스는 별도의 변수에 저장해주고, 비교 인덱스를 현재 인덱스 -1로 잡는다.
> - 별도로 저장해 둔 삽입을 위한 변수와, 비교 인덱스의 배열 값을 비교한다.
> - 삽입 변수의 값이 더 작으면 현재 인덱스로 비교 인덱스의 값을 저장해주고, 비교 인덱스를 -1하여 비교를 반복한다.
> - 만약 삽입 변수가 더 크면, 비교 인덱스+1에 삽입 변수를 저장한다.
>   <br/><br/>
>   시간복잡도 : 최악의 경우 O(n^2) 이미정렬이 완료되 경우 O(n) <br/>
>   공간복잡도 : O(n)

<br/>
<h3>Example</h3>
<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">array&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;list({<span style="color:#c10aff">8</span>,&nbsp;<span style="color:#c10aff">7</span>,&nbsp;<span style="color:#c10aff">6</span>,&nbsp;<span style="color:#c10aff">5</span>,&nbsp;<span style="color:#c10aff">4</span>,&nbsp;<span style="color:#c10aff">3</span>,&nbsp;<span style="color:#c10aff">1</span>,&nbsp;<span style="color:#c10aff">4</span>})</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">for</span>&nbsp;i&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(<span style="color:#c10aff">1</span>,&nbsp;<span style="color:#4be6fa">len</span>(array)):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;key&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;array[i]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;j&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;i<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;j&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">0</span>&nbsp;<span style="color:#ff3399">and</span>&nbsp;key&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;array[j]:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[j],&nbsp;array[j<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;array[j<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>],&nbsp;array[j]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;j&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;array[j<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;key</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<br>

| 장점                                 | 단점                        |
| :----------------------------------- | --------------------------- |
| 최선의 경우 O(n)으로 정렬이 가능하다 | 최악의 경우 O(n^2)이 걸린다 |

---

<br/>
<h2><b>버블 정렬의 경우</b></h2>
<hr><br/>
    
버블 정렬은 매번 연속된 두개 인덱스를 비교하여, 정한 기준의 값을 뒤로 넘겨 정렬하는 방법이다. 오름차순으로 정렬하고자 할 경우, 비교시마다 큰 값이 뒤로 이동하여, 1바퀴 돌 시 가장 큰 값이 맨 뒤에 저장된다. 맨 마지막에는 비교하는 수들 중 가장 큰 값이 저장 되기 때문에, (전체 배열의 크기 - 현재까지 순환한 바퀴 수)만큼만 반복해 주면 된다.

<br/>

> ## 로직
>
> - 버블 정렬은 두 번째 인덱스부터 시작한다. 현재 인덱스 값과, 바로 이전의 인덱스 값을 비교한다.
> - 만약 이전 인덱스가 더 크면, 현재 인덱스와 바꿔준다.
> - 현재 인덱스가 더 크면, 교환하지 않고 다음 두 연속된 배열값을 비교한다.
> - 이를 (전체 배열의 크기 - 현재까지 순환한 바퀴 수)만큼 반복한다.
>   <br/><br/>
>   시간복잡도 : O(n^2) <br/>
>   공간복잡도 : O(n)

<br/>
<h3>Example</h3>
<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">array&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;list({<span style="color:#c10aff">8</span>,&nbsp;<span style="color:#c10aff">7</span>,&nbsp;<span style="color:#c10aff">6</span>,&nbsp;<span style="color:#c10aff">5</span>,&nbsp;<span style="color:#c10aff">4</span>,&nbsp;<span style="color:#c10aff">3</span>,&nbsp;<span style="color:#c10aff">1</span>,&nbsp;<span style="color:#c10aff">4</span>})</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">for</span>&nbsp;i&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(<span style="color:#4be6fa">len</span>(array)<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span>):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">for</span>&nbsp;j&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(<span style="color:#c10aff">1</span>,&nbsp;<span style="color:#4be6fa">len</span>(array)<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>i):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;array[j<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span>]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span>&nbsp;array[j]:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[j<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span>],&nbsp;array[j]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;array[j],&nbsp;array[j<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span>]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>
<br>

| 장점            | 단점                   |
| :-------------- | ---------------------- |
| 구현이 간단하다 | 정렬 시간이 오래걸린다 |

---

<br/>
<h2><b>합병 정렬의 경우</b></h2>
<hr><br/>
    
합병 정렬은 분할 정복(Divide and conquer) 방식으로 설계된 알고리즘, 분할 정복은 큰 문제를 반으로 쪼개 문제를 해결해 나가는 방식이다.
분할은 배열의 크기가 1보다 작거나 같을 때 까지 반복한다. 합병은 두 개의 배열을 비교하여, 기준에 맞는 값을 다른 배열에 저장해 나간다. 결과적으로 입력으로 하나의 배열을 받고, 연산 중에 두개의 배열로 계속 쪼게 나간 뒤, 합치면서 정렬해 최후에는 하나의 정렬을 출력한다.

<br/>

> ## 분할 로직
>
> - 현재 배열을 반으로 쪼깬다. 배열의 시작 위치와, 종료 위치를 입력받아 둘을 더한 후 2를 나눠 그 위치를 기준으로 나눈다.
> - 쪼갠 배열의 크기가 0이거나 1일때 까지 반복한다.
>   <br/><br/>
>
> ## 합병 로직
>
> - 두 배열 A,B의 크기를 비교한다. 각각의 배열의 현재 인덱스를 i,j로 가정
> - i에는 A배열의 시작 인덱스를 저장하고, j에는 B배열의 시작 주소를 저장
> - A[i]와 B[j]를 비교한다. 오름차순의 경우 이중에 작은 값을 새 배열 C에 저장, A[i]가 더 컸다면 A[i]의 값을 배열 C에 저장해주고, i의 값을 하나 증가 시킴
> - 이를 i나 j 둘중 하나가 각자 배열의 끝에 도달할 때 까지 반복
> - 끝까지 저장을 못한 배열의 값을, 순서대로 전부 다 C에 저장
> - C 배열을 원래의 배열에 저장
>   <br/><br/>
>   시간복잡도 : O(nlgn) <br/>
>   공간복잡도 : O(2n)

<br/>
<h3>Example</h3>
<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div><div style="line-height:130%">24</div><div style="line-height:130%">25</div><div style="line-height:130%">26</div><div style="line-height:130%">27</div><div style="line-height:130%">28</div><div style="line-height:130%">29</div><div style="line-height:130%">30</div><div style="line-height:130%">31</div><div style="line-height:130%">32</div><div style="line-height:130%">33</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">def</span>&nbsp;merge_sort(arr):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">def</span>&nbsp;sort(low,&nbsp;high):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;high&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;<span style="color:#c10aff">2</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mid&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;(low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span>&nbsp;high)&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">/</span><span style="color:#0086b3"></span><span style="color:#ff3399">/</span>&nbsp;<span style="color:#c10aff">2</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort(low,&nbsp;mid)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort(mid,&nbsp;high)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;merge(low,&nbsp;mid,&nbsp;high)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">def</span>&nbsp;merge(low,&nbsp;mid,&nbsp;high):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;[]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l,&nbsp;h&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;low,&nbsp;mid</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;l&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;mid&nbsp;<span style="color:#ff3399">and</span>&nbsp;h&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;high:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;arr[l]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;arr[h]:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp.append(arr[l])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp.append(arr[h])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;h&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;l&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;mid:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp.append(arr[l])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;h&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;high:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp.append(arr[h])</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;h&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">for</span>&nbsp;i&nbsp;<span style="color:#ff3399">in</span>&nbsp;<span style="color:#4be6fa">range</span>(low,&nbsp;high):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arr[i]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;temp[i&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;low]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;sort(<span style="color:#c10aff">0</span>,&nbsp;<span style="color:#4be6fa">len</span>(arr))</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>
<br>

| 장점                                     | 단점                            |
| :--------------------------------------- | ------------------------------- |
| 항상 O(NlogN)으로 일정한 속도로 정렬된다 | 추가적인 메모리 공간이 필요하다 |

---

<br/>
<h2><b>퀵 정렬의 경우</b></h2>
<hr><br/>
    
퀵 정렬 또한 분할 정복(Divide and conquer)을 이용하여 정렬을 수행하는 알고리즘이다.
pivot point라고 기준이 되는 값을 하나 설정 하는데, 이 값을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 옮기는 방식으로 정렬을 진행한다.

이를 반복하여 분할된 배열의 크기가 1이되면 배열이 모두 정렬 된 것이다.

<br/>

> ## 로직
>
> - pivot point로 잡을 배열의 값 하나를 정한다. 보통 맨 앞이나 맨 뒤, 혹은 전체 배열 값 중 중간값이나나 랜덤 값으로 정한다.
> - 분할을 진행하기에 앞서, 비교를 진행하기 위해 가장 왼쪽 배열의 인덱스를 저장하는 left 변수, 가장 오른쪽 배열의 인덱스를 저장한 right변수를 생성한다.
> - right부터 비교를 진행한다. 비교는 right가 left보다 클 때만 반복하며. 비교한 배열값이 pivot point보다 크면 right를 하나 감소시키고 비교를 반복한다. pivot point보다 작은 배열 값을 찾으면, 반복을 중지한다.
> - 그 다음 left부터 비교를 진행한다. 비교는 right가 left보다 클 때만 반복하며. 비교한 배열값이 pivot point보다 작으면 left를 하나 증가시키고 비교를 반복한다. pivot point보다 큰 배열 값을 찾으면, 반복을 중지한다.
> - left 인덱스의 값과 right 인덱스의 값을 바꿔준다.
> - 3,4,5 과정을 left<right가 만족 할 때 까지 반복한다.
> - 위 과정이 끝나면 left의 값과 pivot point를 바꿔준다.
> - 맨 왼쪽부터 left - 1까지, left+1부터 맨 오른쪽까지로 나눠 퀵 정렬을 반복한다.
>   <br/><br/>
>
>   시간복잡도 : O(nlgn) 최악일 경우O(n^2) <br/>
>   공간복잡도 : O(nlgn)

<br/>
<h3>Example</h3>
<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">def</span>&nbsp;quick_sort(arr):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">def</span>&nbsp;sort(low,&nbsp;high):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;high&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;low:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mid&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;partition(low,&nbsp;high)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort(low,&nbsp;mid&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;<span style="color:#c10aff">1</span>)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort(mid,&nbsp;high)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">def</span>&nbsp;partition(low,&nbsp;high):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pivot&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;arr[(low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span>&nbsp;high)&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">/</span><span style="color:#0086b3"></span><span style="color:#ff3399">/</span>&nbsp;<span style="color:#c10aff">2</span>]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;high:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;arr[low]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span>&nbsp;pivot:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">while</span>&nbsp;arr[high]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span>&nbsp;pivot:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&lt;</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;high:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arr[low],&nbsp;arr[high]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;arr[high],&nbsp;arr[low]</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low,&nbsp;high&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span>&nbsp;<span style="color:#c10aff">1</span>,&nbsp;high&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;<span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;low</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;sort(<span style="color:#c10aff">0</span>,&nbsp;<span style="color:#4be6fa">len</span>(arr)&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;<span style="color:#c10aff">1</span>)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>
<br>

| 장점                                | 단점                              |
| :---------------------------------- | --------------------------------- |
| 평균시간이 O(NlogN)으로 빠른 편이다 | Pivot에 따라서 성능 차이가 심하다 |
|                                     | 최악의경우 O(n^2)이 걸리게 된다   |

---

# 참고

기본 정렬 알고리즘(Sorting Algoritm) 요약 정리 (선택, 삽입, 버블, 합병, 퀵) : https://hsp1116.tistory.com/33

각 정렬의 특징 및 장단점 & 시간복잡도 : https://coding-factory.tistory.com/615?category=794828

병합 정렬 - Merge Sort : https://www.daleseo.com/sort-merge/

퀵 정렬 - Quick Sort https://www.daleseo.com/sort-quick/
