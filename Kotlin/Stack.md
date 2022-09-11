# 스택 (Stack)

Stack은 후입선출(나중에 입력된 것이 먼저 출력된다)의 구조를 갖는 자료구조이다.
Kotlin에서는 구현된 Stack이 없으므로 사용하기 위해서는 직접 구현하거나 Java에 있는 Stack을 사용할 수 있다.

따라서 사용하기 위해서는 'import java.util.Stack' 을 해주어야 한다.

    public class Stack<E> extends Vector<E>

제네릭을 사용하는 스택 클래스
</br>

    val stack = Stack<Int>()

int 자료형으로 구성된 스택을 생성

## 시간 복잡도

- 접근, 검색 - O(n) [처음 Index부터 순회]

- 추가, 삭제 - O(1) [마지막 index에 대해서 추가, 삭제 보장]

<br/><br/>

# 메서드

## push()

    public E push​(E item) // Pushes an item onto the top of this stack.

Stack에 최상단 항목으로 삽입한다.

## pop()

    public E pop() // Removes the object at the top of this stack and returns that object as the value of this function.
    // EmptyStackException - if this stack is empty.

Stack의 최상단에 있는 객체를 제거하고 해당 객체를 return한다.

## peek()

    public E peek() // Looks at the object at the top of this stack without removing it from the stack.
    // EmptyStackException - if this stack is empty.

Stack에서 제거하지 않고 스택의 최상단(맨 위)에 있는 객체를 확인한다.

## empty()

    public boolean empty() // Tests if this stack is empty.

Stack이 비어있다면 true, 아니면 false를 반환한다.

## serach()

    public int search​(Object o) // Returns the 1-based position where an object is on this stack.

Object를 Stack에서 찾는 method로 최상단 객체를 1로 하여(1-based-position) 위치(position)를 찾아주며, 객체가 없다면 -1을 return한다.

### Methods declared in class java.util.Vector

add, add, addAll, addAll, addElement, capacity, clear, clone, contains, containsAll, copyInto, elementAt, elements, ensureCapacity, equals, firstElement, forEach, get, hashCode, indexOf, indexOf, insertElementAt, isEmpty, iterator, lastElement, lastIndexOf, lastIndexOf, listIterator, listIterator, remove, remove, removeAll, removeAllElements, removeElement, removeElementAt, removeIf, removeRange, replaceAll, retainAll, set, setElementAt, setSize, size, spliterator, subList, toArray, toArray, toString, trimToSize

### Methods declared in class java.lang.Object

finalize, getClass, notify, notifyAll, wait, wait, wait

### Methods declared in interface java.util.Collection

parallelStream, stream, toArray

### Methods declared in interface java.util.List

sort
<br/><br/>

# 참고

Oracle : https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Stack.html#empty()

[Kotlin] 자료구조 1 (배열, 스택, 큐, 링크드리스트) : https://genius-dev.tistory.com/entry/Kotlin%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Stack%EA%B3%BC-Queue%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC
