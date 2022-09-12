# 링크드리스트 (Linked List)

Linked List는 각 요소 내에 다음 요소를 가리키는 Pointer가 존재하여 연결되는 구조이다.
즉 노드를 연속적으로 연결함으로써 배열과 달리 동적인 크기를 가지고 있으며 메모리 공간에 모여있지 않고 산재되어질 수 있다(non-continuous).

Kotlin에서는 참조를 통해 서로를 연결됩니다. 따라서 사용하기 위해서는 'import java.util.\*'를 해주어야만 합니다.

## Linked List

    public class LinkedList<E> extends AbstractSequentialList<E> implements List<E>, Deque<E>, Cloneable, Serializable

제네릭을 사용하고 AbstractSequentialList를 상속받고 List, Deque, Cloneable, Serializable를 참조하는 LinkedList 클래스

    static class Node<E> {
        E item;
        Node<E> next;
        Node<E> prev;

        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }

Java에 구현되어 있는 LinkedList의 각 요소인 Node class

    val linkedList = LinkedList<Int>()

</br>

## 시간 복잡도

- 접근, 검색 - O(n) [처음 Index부터 순회]

- 추가, 삭제 - 맨 앞 또는 뒤라면 O(1), 중간 위치라면 O(n)

</br>

# 메서드

## getFirst

    public E getFirst() // Returns the first element in this list.

list의 첫번째 값을 반환합니다.

### Exception

NoSuchElementException - if this list is empty, list에 담겨진 값이 없으면 발생

</br>

## getLast

    public E getLast() // Returns the last element in this list.

list의 마지막 값을 반환합니다.

### Exception

NoSuchElementException - if this list is empty, list에 담겨진 값이 없으면 발생

</br>

## removeFirst

    public E removeFirst() // Removes and returns the first element from this list.

list의 첫번째 값을 반환하고 값을 삭제합니다.

### Exception

NoSuchElementException - if this list is empty, list에 담겨진 값이 없으면 발생

</br>

## removeLast

    public E removeLast() // Removes and returns the last element from this list.

list의 마지막 값을 반환하고 값을 삭제합니다.

### Exception

NoSuchElementException - if this list is empty, list에 담겨진 값이 없으면 발생

</br>

## addFirst

    public void addFirst​(E e) // Inserts the specified element at the beginning of this list.

list의 첫번째에 값을 추가합니다.

</br>

## addLast

    public void addLast​(E e) // Appends the specified element to the end of this list.

list의 첫번째에 값을 추가합니다. add(E)랑 역할을 같습니다.

</br>

## contains

    public boolean contains​(Object o) // Returns true if this list contains the specified element. More formally, returns true if and only if this list contains at least one element e such that Objects.equals(o, e).

list에 해당값의 유무를 boolean형태로 반환합니다. Objects.equals(o, e)와 역할을 같습니다.

</br>

## size

    public int size() // Returns the number of elements in this list.

list의 size를 반환합니다.

</br>

## add

    public void add​(E element) // Appends the specified element to the end of this list.

리스트의 끝에 값을 추가

    public void add​(int index, E element) // Inserts the specified element at the specified position in this list.

해당 index에 element를 추가합니다. 뒤에 있는 내용은 밀려 납니다.

</br>

## addAll

    public boolean addAll​(Collection<? extends E> c) // Appends all of the elements in the specified collection to the end of this list, in the order that they are returned by the specified collection's iterator.

리스트의 끝에 값들을 추가

public boolean addAll​(int index, Collection<? extends E> c) // Inserts all of the elements in the specified collection into this list, starting at the specified position.

해당 index에 값들을 추가합니다. 뒤에 있는 내용은 밀려 납니다.

### Exception

NullPointerException - if the specified collection is null
IndexOutOfBoundsException - if the index is out of range (index < 0 || index > size())

</br>

## remove

    public E remove() // Retrieves and removes the head (first element) of this list.

리스트의 Head값을 반환하고 삭제합니다.

    public E remove​(int index) //Removes the element at the specified position in this list.

리스트의 index값에 있는값을 반환하고 삭제합니다.

    public boolean remove​(Object o) // Removes the first occurrence of the specified element from this list, if it is present.

해당값이 있으면 삭제를하고 true를 발생시키고 없을경우 false를 반환합니다. 삭제를 시킬경우 Head에서 Last까지 탐색하여 첫번째로 나온 index만 삭제시킵니다. NoSuchElementException은 발생시지는 않습니다. int 자료형의 값을 줄경우 remove​(index)가 호출되기 때문에 removeFirstOccurrence나 removeLastOccurrence를 권유함

### Exception

NoSuchElementException - if this list is empty

</br>

## removeFirstOccurrence

    public boolean removeFirstOccurrence​(Object o) // Removes the first occurrence of the specified element in this list (when traversing the list from head to tail). If the list does not contain the element, it is unchanged.

해당값이 있으면 삭제를하고 true를 발생시키고 없을경우 false를 반환합니다. 삭제를 시킬경우 Head에서 Last까지 탐색하여 첫번째로 나온 index만 삭제시킵니다.

</br>

## removeLastOccurrence

    public boolean removeLastOccurrence​(Object o) // Removes the last occurrence of the specified element in this list (when traversing the list from head to tail). If the list does not contain the element, it is unchanged.

해당값이 있으면 삭제를하고 true를 발생시키고 없을경우 false를 반환합니다. 삭제를 시킬경우 Last에서 Head까지 탐색하여 첫번째로 나온 index만 삭제시킵니다.

</br>

## clear

    public void clear() // Removes all of the elements from this list. The list will be empty after this call returns.

list를 모든 값들을 삭제합니다.

</br>

## get

    public E get​(int index) // Returns the element at the specified position in this list.

해당 index의 값을 가져옵니다.

### Exception

IndexOutOfBoundsException - if the index is out of range (index < 0 || index >= size())

<br/><br/>

# 참고

Oracle : https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/LinkedList.html#removeFirstOccurrence(java.lang.Object)

add와 offer의 차이, remove와 poll, element와 peek의 차이 ... : https://kotlinworld.com/8
