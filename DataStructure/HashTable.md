# 해시테이블

<br/>

    해시 테이블은 (Key, Value)로 데이터를 저장하는 자료구조 중 하나로 빠르게 데이터를 검색할 수 있는 자료구조입니다.
    해시 테이블이 빠른 검색속도를 제공하는 이유는 내부적으로 배열(버킷)을 사용하여 데이터를 저장하기 때문입니다.
    해시 테이블은 각각의 Key값에 해시함수를 적용해 배열의 고유한 index를 생성하고, 이 index를 활용해 값을 저장하거나 검색하게 됩니다.
    여기서 실제 값이 저장되는 장소를 버킷 또는 슬롯이라고 합니다.

<br/>

<br/>
<h2><b>기능</b></h2>
<br/>

데이터 삽입(저장)

- Hash table 에서 데이터를 저장하기 위해서는 먼저 hach function 을 이용하여 key 값을 hash 로 변경합니다.
- 이후 미리 준비해둔 저장소(bucket, slot) 중에 알맞는 hash 값을 찾아 value 를 저장합니다.

- 해시 충돌이 일어나지 않는다는 가정하에 데이터 삽입(저장) 과정의 시간복잡도는 O(1) 입니다.
  <br/><br/>

데이터 삭제

- 저장되어 있는 값을 삭제가기 위해서는 bucket 에서 삭제하려고하는 key 와 매칭되는 value 값을 찾아서 삭제합니다.
- 해시 충돌이 일어나지 않는다는 가정하에 데이터 삭제 과정의 시간복잡도는 O(1) 입니다.
  <br/><br/>

데이터 검색

- key 를 이용해 value 를 찾아내는 과정입니다. 먼저 key값과 hash function 을 이용해 hash 를 찾아내고 해당 hash 로 value 값을 찾을 수 있습니다.

- 해시 충돌이 일어나지 않는다는 가정하에 데이터 검색 과정의 시간복잡도는 O(1) 입니다.

<br/>
<h2><b>해시 충돌</b></h2>
<br/>

여러 key 에 해당하는 hash(주소)가 동일한 경우를 해시 충돌(Hash Collision)이라고 부릅니다.

비둘기집의 원리로 인해 hash 를 이용한 자료구조에서는 무조전적으로 일어날 수 밖에 없는 현상입니다.

Chaning (Open Hashing)

- Chaining 방법은 해시 충돌이 발생했을 때 이를 동일한 bucket에 저장 하되 나중에 저장되는 값을 연결리스트 형태로 저장하는 방법입니다.
- linked list 의 요소들을 처음부터 하나씩 찾아야하므로 시간복잡도는 O(n) 까지 늘어날 수도 있다는 단점이 있습니다.

Open Addressing (Close hashing)

- Open Addressing 방법은 해시 충돌이 일어날 경우, 비어있는 hash를 찾아 데이터를 저장하는 기법입니다.
- 비어있는 hash 를 찾는 방법으로 단순히 한칸씩 옆으로 옮기며 빈 공간(bucket) 를 찾아가는 linear probing 방법이 있습니다.
  - 이러한 linear probing 방법을 사용하면 데이터들이 특정 위치에만 밀집하는 clustering 문제가 발생할 수 있습니다.
- n의 제곱만큼 건너뛰어 빈 공간(bucket) 를 찾아가는 quadratic probing 방법도 있습니다.

<br/>
<h2><b>결론</b></h2>
<br/>

데이터 저장, 삭제, 검색이 많이 필요한 경우에 사용하기 좋은 하지만 해시충돌의 경우도 생각해야합니다.

<br/><br/>

# 참고

[자료구조] 해시테이블(HashTable)이란? : https://mangkyu.tistory.com/102

자료구조(Data Structure) 톺아보기 - 해시(Hash) : https://ai-rtistic.com/2022/01/29/data-structure-hash/
