# 이진 탐색 알고리즘

<br/>

    이진 탐색, 정렬된 리스트에서 검색 범위를 줄여 나가면서 검색 값을 찾는 알고리즘

<br/>

<br/>
<h2><b>로직 및 구현</b></h2>
<hr><br/>

    중간 값을 찾아야 하기 때문에  반드시 정렬된 배열에서만 사용할 수 있습니다

> ## 로직
>
> - 배열의 중간 값을 가져옵니다.
> - 중간 값과 검색 값을 비교합니다.
>
>   - 중간 값이 검색 값과 같다면 종료합니다
>   - 중간 값보다 검색 값이 크다면 중간값 기준 배열의 오른쪽 구간을 대상으로 탐색합니다.
>   - 중간 값보다 검색 값이 작다면 중간값 기준 배열의 왼쪽 구간을 대상으로 탐색합니다.
>
>   <br/>
>
> 시간복잡도
>
> - Best : O(1)
> - Average : Θ(log n)
> - Worst : O(log n)

<br/>
<h3>Example</h3>
<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">def</span>&nbsp;binarySearch(arr,&nbsp;low,&nbsp;high,&nbsp;key):</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span>&nbsp;high:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;mid&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;low&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">+</span>&nbsp;(high&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">-</span>&nbsp;low)<span style="color:#0086b3"></span><span style="color:#ff3399">/</span><span style="color:#c10aff">2</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">if</span>&nbsp;arr[mid]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span><span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;key:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;mid</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">elif</span>&nbsp;arr[mid]&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">&gt;</span>&nbsp;key:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;binarySearch(arr,&nbsp;low,&nbsp;mid<span style="color:#0086b3"></span><span style="color:#ff3399">-</span><span style="color:#c10aff">1</span>,&nbsp;key)</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">else</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">return</span>&nbsp;binarySearch(arr,&nbsp;mid<span style="color:#0086b3"></span><span style="color:#ff3399">+</span><span style="color:#c10aff">1</span>,&nbsp;high,&nbsp;key)</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>
<br>

| 장점                                                                | 단점                             |
| :------------------------------------------------------------------ | -------------------------------- |
| 검색이 반복될 때마다 검색 범위가 절반으로 줄기 때문에 속도가 빠르다 | 정렬된 리스트에만 사용할 수 있다 |

# 참고

이진 탐색 (Binary search) 개념 및 : https://yoongrammer.tistory.com/75
