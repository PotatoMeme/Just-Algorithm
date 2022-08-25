def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


void merge(vector < int > & v, int s, int e, int m) {
    vector < int > ret
    int i = s, j = m + 1, copy = 0

    // 결과를 저장할 배열에 하나씩 비교하여 저장한다.
    while (i <= m & & j <= e) {
        if (v[i] < v[j])ret.push_back(v[i++])
        else if (v[i] > v[j])ret.push_back(v[j++])
    }

    // 남은 값들을 뒤에 채워넣어준다.
    while (i <= m)  ret.push_back(v[i++])
    while (j <= e)  ret.push_back(v[j++])

    // 원래 배열에 복사해준다.
    for (int k=s
         k <= e
         k++) {
        v[k] = ret[copy++]
    }
}

//합병 정렬
void mergeSort(vector < int > & v, int s, int e){
    if(s < e){
        int m = (s+e)/2
        / *divide, 분할*/
        mergeSort(v, s, m)
        // s부터 m까지
        mergeSort(v, m+1, e)
        // m+1부터 e까지
        / *conquer, 합병*/
        merge(v, s, e, m)
    }
}
