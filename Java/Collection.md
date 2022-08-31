# 컬렉션(Collection)

<br/>

    Java에서 컬렉션은 다수의 요소를 하나의 그룹으로 묶어 효율적으로 저장하고, 관리할 수 있는 기능을 제공하는 일종의 컨테이너입니다.

    JCF(Java Collections Framework)는 이러한 데이터, 자료구조인 컬렌션과 이를 구현하는 클래스를 정의하는 인터페이스를 제공합니다.

<br/>
<h2><b>이점</b></h2>
<br/>

- List, Queue, Set, Map 등의 인터페이스를 제공하고, 이를 구현하는 클래스를 제공하여 일관된 API 를 사용할 수 있습니다.
- 가변적인 저장 공간을 제공한다.
- 자료구조, 알고리즘을 구현하기 위한 코드를 직접 작성할 필요 없이, 이미 구현된 컬렉션 클래스를 목적에 맞게 선택하여 사용할수 있습니다.
- 제공되는 API 의 코드는 검증되었으며, 고도로 최적화 되어있습니다.
- JDK에서 지원을 해주기때문에 유지보수하기 쉽게 만들어줍니다.

<br/>
<h2><b>구조</b></h2>
<br/>

대표적으로 List , Queue , Set , Map 인터페이스로 구성되어 있으며, 세부적으로 여러 클래스가 해당 인터페이스를 구현하거나, 다른 인터페이스가 상속받는 구조로 되어있습니다.

Queue 는 인터페이스는 존재하나, 직접 구현된 클래스는 존재하지 않습니다.

Queue 를 구현하려면 LinkedList 를 사용하여 구현할 필요가 있습니다.

PriorityQueue 는 FIFO 가 아닌, 요소의 우선순위에 따라 출력 순서가 바뀌므로 일반적인 Queue 가 아닙니다.

Map의 경우 Collection 인터페이스를 상속받고 있지 않지만 Collection으로 분류됩니다.

<br/>
<h2><b>인터페이스별 특징</b></h2>
<br/>

| 인터페이스    | 구현클래스                    | 특징                                                                                                    |
| :------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- |
| 집합 (Set)    | HashSet, TreeSet              | 순서가 없으며, 데이터를 중복하여 저장할 수 없다. 집합 연산 (합집합, 교집합, 차집합 등) 을 지원한다.     |
| 리스트 (List) | LinkedList, Vector, ArrayList | 인덱스 순서로 요소를 저장한다. 중복된 데이터를 저장할 수 있다.                                          |
| 큐 (Queue)    | LinkedList, PriorityQueue     | 데이터가 저장된 순서대로 출력되는 선입선출 (FIFO: First In First Out) 의 구조를 갖는 선형 자료구조이다. |
| 맵 (Map)      | Hashtable, HashMap, TreeMap   | Key-value 쌍으로 데이터를 저장한다. 순서가 존재하지 않으며, Key 가 중복될 수 없다.                      |

<br/><br/>

# 참고

[JAVA] Java 컬렉션(Collection) 정리: https://gangnam-americano.tistory.com/41

JAVA Collection Framework (1) - 컬렉션 프레임워크란? : https://hudi.blog/java-collection-framework-1/
