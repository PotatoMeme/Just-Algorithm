# 덱(Dequeue)

<br/>

    덱 (Deque)은 Double-ended queue를 줄인 것으로, 양쪽에서 삽입과 삭제가 가능한 구조이며 스택과 큐의 연산을 모두 지원한다.
    즉, 앞쪽 front와 뒤쪽 rear에서 모두 삽입과 삭제가 가능한 큐를 의미한다. 따라서 스택과 큐의 특성을 모두 갖는 자료구조이다.

<br/>
<h2><b>연산 종류</b></h2>
<br/>

- append() : 오른쪽에서 데이터를 삽입

- appendleft() : 왼쪽에서 데이터를 삽입

- pop() : 오른쪽에서 데이터 삭제

- popleft() : 왼쪽에서 데이터 삭제

<br/>
<h2><b>활용</b></h2>
<br/>

덱을 활용한 다이나믹 프로그래밍

- 동적 계획법(DP)의 최적화 기법 중 하나입니다.
- 보통 Monotone Stack 테크닉처럼 Monotone Deque을 활용하여 점화식을 수행합니다.

<br/><br/>

# 참고

덱 (자료 구조) : https://ko.wikipedia.org/wiki/%EB%8D%B1_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)

_8_ 자료구조 — 덱 : https://medium.com/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%80-%EB%AF%B8%EC%B9%9C%EC%A7%93%EC%9D%B4%EB%8B%A4/8-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EB%8D%B1-8090a6f9feaa
