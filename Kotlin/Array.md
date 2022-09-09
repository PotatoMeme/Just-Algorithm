# 배열 (Array)

같은 type의 연관된 데이터를 효율적으로 관리하기 위한 자료구조.


- 장점 : index를 통해 원하는 위치에 있는 값에 대해 효율적으로 접근 할 수 있음.

- 단점 : 크기가 정해져 있으므로 유동적인 데이터의 추가, 삭제가 어려움.

## Array

    class Array<T>

제네릭을 사용하는 배열 클래스

    <init>(size: Int, init: (Int) -> T)

생성자 size 와 init이라는 람다 함수를 매개변수로 가짐

    // ex)
    
    // 크기 5의 배열 
    // [0, 0, 0, 0, 0]
    val array: Array<Int> = Array(5) { 0 }
    //Array(5, { 0 })

## 다차원 배열

    var array = Array(3) { Array(4) { 0 } }

- 시간 복잡도 : 

  - 접근 - O(1) [Index를 통해 값에 바로 접근]

  - 검색 - O(n) [처음 Index부터 순회]

  - 추가, 삭제 - 맨 뒤에 추가, 삭제 시 O(1), 중간 값일 시 추가, 삭제 후 데이터를 한칸씩 밀어야 하므로 O(n)


# 메서드

## arrayOf
    
    fun <T> arrayOf(vararg elements: T): Array<T>

제네릭배열을 반환하는 함수 매개변수의 개수만큼의 크기를 가지고 매개변수를 넣은 순서대로 그값이 들어감

arrayOf()에 특정 타입을 지정하지 않는다면 배열에 어떤 값이 들어가도 상관없다.


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
    

## size, lastIndex

    val size: Int // Returns the number of elements in the array.
    val <T> Array<out T>.lastIndex: Int // Returns the last valid index for the array.

해당배열의크기와 마지막 index값을 가져옵니다.

    val array: Array<Int> = arrayOf(1, 2, 3)
    
    print(array.size) // 3
    print(array.lastIndex) // 2

lastIndex = size-1

## indices

    val <T> Array<out T>.indices: IntRange

array의 크기만큼을 intRange로 변환

    val array: Array<Int> = arrayOf(31, 22, 53)

    print(array.indices)//0,1,2

## sum() , average()

    fun Array<out Byte>.sum(): Int
    fun Array<out Short>.sum(): Int
    fun Array<out Int>.sum(): Int
    fun Array<out Long>.sum(): Long
    fun Array<out Float>.sum(): Float
    fun Array<out Double>.sum(): Double

    // Returns the sum of all elements in the array.

배열의 합을 반환하는 sum

    fun Array<out Byte>.average(): Double
    fun Array<out Short>.average(): Double
    fun Array<out Int>.average(): Double
    fun Array<out Long>.average(): Double
    fun Array<out Float>.average(): Double
    fun Array<out Double>.average(): Double

    // Returns an average value of elements in the array.


배열의 평균을 반환하는 average

    val array = arrayOf(1,2,3)

    println(array.sum()) // 6
    println(array.average()) // 2.0 : Double

## sort


기존 배열 정렬

    val array1 = arrayOf(2,1,3)

	array1.sort()
    println(array1.contentToString()) // [1, 2, 3]

## sortedArray() , sortedArrayDescending()

오름차순/내림차순 정렬한 새로운 배열 생성
    val array1 = arrayOf(2,1,3)

	val sorted = array1.sortedArray()  // [1,2,3]
    val sortedDescending() = array1.sortedArrayDescending() //[3,2,1]

## sorted, sortedDescending()
정렬된 List 변환

    val listFromArray : List<Int> = array1.toList()
    val sortedListFromArray : List<Int> = array1.sorted()
    val sortedDescendingListFromArray = array1.sortedArrayDescending()

<br/><br/>

# 참고

Package kotlin : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/


[Kotlin] 자료구조 1 (배열, 스택, 큐, 링크드리스트)
 : https://hungseong.tistory.com/39

 코틀린 자료구조 - 배열(Array) : 
 https://velog.io/@ashwon1218/%EC%BD%94%ED%8B%80%EB%A6%B0-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EB%B0%B0%EC%97%B4Array