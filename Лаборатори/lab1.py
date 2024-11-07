import unittest
import json

def find_max(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)
    return max(left_max, right_max)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        l1 = a[:mid]
        l2 = a[mid:]

        merge_sort(l1)
        merge_sort(l2)

        i = j = k = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                a[k] = l1[i]
                i += 1
            else:
                a[k] = l2[j]
                j += 1
            k += 1
        
        while i < len(l1):
            a[k] = l1[i]
            i += 1
            k += 1
        
        while j < len(l2):
            a[k] = l2[j]
            j += 1
            k += 1

def binary_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)
    else:
        return binary_search(arr, low, mid - 1, target)

class TestSorting(unittest.TestCase):

    def setUp(self):
        with open('input.txt', 'r') as file:
            json_data = file.read()  
            data = json_data.split('\t')  
            
            self.arr = json.loads(data[0])  
            self.CorAns = json.loads(data[1])
            self.Target = json.loads(data[2]) 

    def testSort(self):
        arr_copy = self.arr.copy()
        insertion_sort(arr_copy)
        self.assertEqual(arr_copy, self.CorAns)

    def testMergeSort(self):
        arr_copy = self.arr.copy()
        merge_sort(arr_copy)
        self.assertEqual(arr_copy, self.CorAns)

    def testMax(self):
        max_element = find_max(self.arr, 0, len(self.arr) - 1)
        self.assertEqual(max_element, max(self.arr)) 

    def testBinarySearch(self):
        sorted_arr = sorted(self.arr)
        target_value = self.Target if isinstance(self.Target, int) else self.Target[0]
        
        result_index = binary_search(sorted_arr, 0, len(sorted_arr) - 1, target_value)
        expected_index = sorted_arr.index(target_value) if target_value in sorted_arr else -1
        self.assertEqual(result_index, expected_index)

if __name__ == '__main__':
    unittest.main()
