# 스택

<br/>

    스택이란 한쪽 끝에서만 데이터를 넣고 뺄 수 있는 제한적으로 접근할 수 있는 후입선출(Last-In-First-Out) 형태의 선형 자료구조입니다
    기본적으로 Stack 클래스는 내부에서 최상위 타입 배열인 Object[] 배열을 사용하여 데이터를 관리하고 있습니다.

<br/>
<h2><b>연산 종류</b></h2>
<br/>

- pop() : 스택에서 가장 위에 있는 항목을 제거한다.

- push(item) : item 하나를 스택의 가장 윗 부분에 추가한다.

- peek() : 스택의 가장 위에 있는 항목을 반환한다.

- isEmpty() : 스택이 비어 있을 때 true를 반환한다.

<br/>
<h2><b>구조</b></h2>
<br/>

- Bottom : 가장 밑에 있는 데이터 또는 인덱스

- Top : 가장 위에 있는 데이터 또는 인덱스

- Capacity : 스택에 담을 수 있는 데이터의 총 용량

- Size : 현재 스택에 담겨져있는 데이터의 개수

<br/>
<h2><b>시간복잡도</b></h2>
<br/>

스택의 삽입이나 삭제시 맨 위의 데이터를 삭제하기 때문에 시간복잡도는 늘 O(1) 이다. 하지만 특정 데이터를 찾을때는 데이터를 찾을때까지 순차적으로 수행해야 하므로 O(n) 시간복잡도를 갖는다.

<br/>
<h2><b>활용</b></h2>
<br/>

재귀적으로 함수를 호출하는 경우에 임시 데이터를 스택에 넣어 주고, 빠져 나와 백 트래킹을 할 때는 스택에 넣어 두었던 임시 데이터를 빼 주는 형식으로 사용하면 된다.

또한 스택은 재귀 알고리즘을 반복적 형태를 통해서 구현할 수 있게 해준다.

<br/>
<h2><b>결론</b></h2>
<br/><br/>

스택은 LIFO이기 때문에 최근 데이터를 찾는경우인 히스토리를 구현할때등 뒤로가는 기능을 만들때유용하다.
또한 재귀함수에서도 유용하게 쓰인다.

<br/><br/>

# 참고

[자료구조] | 스택(Stack) : https://velog.io/@alkwen0996/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack