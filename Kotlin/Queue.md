# 큐 (Queue)

한쪽 끝에서는 삽입, 한쪽 끝에서는 추출 작업이 이루어짐.
Kotlin 에서는 Stack처럼 구현된 것이 없어 직접 구현하거나 혹은 Java에서 사용하였던 LinkedList와 Queue를 사용할 수 있다.

따라서 사용하기 위해서는 'import java.util.\*'를 해주어야만 한다.

## Queue

    public interface Queue<E> extends Collection<E>

제네릭을 사용하고 Collection을 상속받는 Queue 규칙

    val queue: Queue<Int> = LinkedList()

LinkedList를 이용하여 생성된 Queue는 Capacity가 지정되어 있지 않으며 계속해서 값을 넣을수 있다.

    val queue: Queue<Int> = LinkedList(intArrayOf(1,2,3).asList())

Array가 있을 때는 list로 바꾿다음 LinkedList의 생성자에 넣어주면 됩니다

LinkedList이외에도 구현하는 다양한 클래스가 존재한다.( AbstractQueue, ArrayBlockingQueue, ArrayDeque, ConcurrentLinkedDeque, ConcurrentLinkedQueue, DelayQueue, LinkedBlockingDeque, LinkedBlockingQueue, LinkedList, LinkedTransferQueue, PriorityBlockingQueue, PriorityQueue, SynchronousQueue 등)

</br>

## 시간 복잡도

- 접근, 검색 - O(n) [처음 Index부터 순회]

- 추가, 삭제 - O(1) [ 마지막 index에 추가, 처음 index 대해서 삭제 보장]

</br>

# 메서드

## add

    boolean add​(E e)

큐에 값을 넣는 함수, Capacity로 인한 오류가 발생할수 있음. LinkedList에서는 메모리 한계까지 만들지 않는이상 오류가 발생하지않음 용량에 제한이있지 않는이상 써도 문제는 없음

    // ex)

    val queue: Queue<Int> = LinkedList()
    queue.add(5)
    queue.add(3)
    print(queue) // 5,3

### Exception

IllegalStateException - if the element cannot be added at this time due to capacity restrictions

ClassCastException - if the class of the specified element prevents it from being added to this queue

NullPointerException - if the specified element is null and this queue does not permit null elements

IllegalArgumentException - if some property of this element prevents it from being added to this queue

</br>

## offer

    boolean offer​(E e)

큐에 값을 넣는 함수

    // ex)

    val queue: Queue<Int> = LinkedList()
    queue.offer(5)
    queue.offer(3)
    print(queue) // 5,3

### Exception

ClassCastException - if the class of the specified element prevents it from being added to this queue

NullPointerException - if the specified element is null and this queue does not permit null elements

IllegalArgumentException - if some property of this element prevents it from being added to this queue

</br>

## remove

    E remove()

큐에 값을 빼내는함수, 빼낸값을 리턴합니다. 더이상 값이 없을 경우 NoSuchElementException 을 발생시킵니다

    // ex)

    val queue: Queue<Int> = LinkedList(intArrayOf(1,2).asList())
    print(queue.remove()) // 1
    print(queue.remove()) // 2
    print(queue.remove()) // NoSuchElementException

### Exception

NoSuchElementException - if this queue is empty

</br>

## poll

    E poll()

큐에 값을 빼내는함수, 빼낸값을 리턴합니다. 더이상 값이 없을 경우 null을 반환합니다.

    // ex)

    val queue: Queue<Int> = LinkedList(intArrayOf(1,2).asList())
    print(queue.poll()) // 1
    print(queue.poll()) // 2
    print(queue.poll()) // null

</br>

## element

    E element()

큐에 값을 Head에 어떤값이 있는지 확인하는함수. 더이상 값이 없을 경우 NoSuchElementException 을 발생시킵니다

    // ex)

    val queue: Queue<Int> = LinkedList(intArrayOf(1,2).asList())
    print(queue.remove()) // 1
    print(queue.remove()) // 2
    print(queue.element()) // NoSuchElementException

### Exception

NoSuchElementException - if this queue is empty

## peek

    E peek()

큐에 값을 Head에 어떤값이 있는지 확인하는함수.

    // ex)

    val queue: Queue<Int> = LinkedList(intArrayOf(1,2).asList())
    print(queue.remove()) // 1
    print(queue.remove()) // 2
    print(queue.peek()) // null

<br/><br/>

# 참고

Oracle : https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Queue.html

add와 offer의 차이, remove와 poll, element와 peek의 차이 ... : https://kotlinworld.com/8
