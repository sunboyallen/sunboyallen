#include <iostream>
using namespace std;

int main()
{
    cout << "ok" << endl;
}

// 将数组进行快速排序的函数
void quickSort(int *arr, int left, int right)
{
    if (left >= right)
        return;
    int i = left, j = right;
    int key = arr[left];
    while (i < j)
    {
        while (i < j && arr[j] >= key)
            j--;
        arr[i] = arr[j];
        while (i < j && arr[i] <= key)
            i++;
        arr[j] = arr[i];
    }
    arr[i] = key;
    quickSort(arr, left, i - 1);
    quickSort(arr, i + 1, right);
}


