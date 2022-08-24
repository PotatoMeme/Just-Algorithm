# 정렬 알고리즘

<br/>

    정렬 알고리즘, n개의 숫자가 입력으로 주어졌을때 이를 문제의 기준과 맞게 정렬하여 출력하는 알고리즘

    이러한 정열알고리즘 문제같은경우 선택 정렬, 삽입 정렬, 버블 정렬, 합병 정렬, 퀵 정렬등으로 나눌수 있습니다.

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
