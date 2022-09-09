# 배열 (Array)

같은 type의 연관된 데이터를 효율적으로 관리하기 위한 자료구조.

- 장점 : index를 통해 원하는 위치에 있는 값에 대해 효율적으로 접근 할 수 있음.

- 단점 : 크기가 정해져 있으므로 유동적인 데이터의 추가, 삭제가 어려움.

- 시간 복잡도 : 

  - 접근 - O(1) [Index를 통해 값에 바로 접근]

  - 검색 - O(n) [처음 Index부터 순회]

  - 추가, 삭제 - 맨 뒤에 추가, 삭제 시 O(1), 중간 값일 시 추가, 삭제 후 데이터를 한칸씩 밀어야 하므로 O(n)

## arrayOf
    
    fun <T> arrayOf(vararg elements: T): Array<T>

제네릭배열을 반환하는 함수 매개변수의 개수만큼의 크기를 가지고 매개변수를 넣은 순서대로 그값이 들어감

    // ex)

    // 크기 3의 배열 
    // [1, 2, 3]
    val array: Array<Int> = arrayOf(1, 2, 3)

## arrayOfNulls

    fun <reified T> arrayOfNulls(size: Int): Array<T?>

size 만큼의 크기를 갖는 null로 이루어진배열을 반환하는 함수

    // ex)

    // 크기 3의 배열 
    // [null, null, null]
    val array: Array<Int> = arrayOfNulls(3)
    
## Array

    class Array<T>

제네릭을 사용하는 배열 클래스

    <init>(size: Int, init: (Int) -> T)

생성자 size 와 init이라는 람다 함수를 매개변수로 가짐

    // ex)
    
    // 크기 5의 배열 
    // [0, 0, 0, 0, 0]
    val array3: Array<Int> = Array(5) { 0 }
    //Array(5, { 0 })

## indices

    val <T> Array<out T>.indices: IntRange

array의 크기만큼을 intRange로 변환


<br/><br/>

# 참고

Package kotlin : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/


[Kotlin] 자료구조 1 (배열, 스택, 큐, 링크드리스트)
 : https://hungseong.tistory.com/39