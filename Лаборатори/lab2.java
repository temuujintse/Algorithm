import java.util.Arrays;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class lab2 {

    public static int findMax(int[] arr, int low, int high) {
        if (low == high) {
            return arr[low];
        }
        int mid = (low + high) / 2;
        int leftMax = findMax(arr, low, mid);
        int rightMax = findMax(arr, mid + 1, high);

        return Math.max(leftMax, rightMax);
    }

    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i;
            while (j > 0 && arr[j - 1] > key) {
                arr[j] = arr[j - 1];
                j--;
            }
            arr[j] = key;
        }
    }

    public static void mergeSort(int[] a) {
        if (a.length > 1) {
            int mid = a.length / 2;
            int[] l1 = Arrays.copyOfRange(a, 0, mid);
            int[] l2 = Arrays.copyOfRange(a, mid, a.length);

            mergeSort(l1);
            mergeSort(l2);

            int i = 0, j = 0, k = 0;
            while (i < l1.length && j < l2.length) {
                if (l1[i] <= l2[j]) {
                    a[k] = l1[i];
                    i++;
                } else {
                    a[k] = l2[j];
                    j++;
                }
                k++;
            }

            while (i < l1.length) {
                a[k] = l1[i];
                i++;
                k++;
            }

            while (j < l2.length) {
                a[k] = l2[j];
                j++;
                k++;
            }
        }
    }

    public static int binarySearch(int[] arr, int low, int high, int target) {
        if (low > high) {
            return -1;
        }

        int mid = (low + high) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binarySearch(arr, mid + 1, high, target);
        } else {
            return binarySearch(arr, low, mid - 1, target);
        }
    }

    private int[] arr;
    private int[] corAns;
    private int target;

    @Before
    public void setUp() throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            String[] data = br.readLine().split("\t");
            arr = parseArray(data[0]);  
            corAns = parseArray(data[1]); 
            target = Integer.parseInt(data[2].trim()); 
        }
    }

    private int[] parseArray(String arrayStr) {
        // Remove square brackets and whitespace, then split by commas
        arrayStr = arrayStr.replaceAll("[\\[\\] ]", "");
        return Arrays.stream(arrayStr.split(","))
                     .mapToInt(Integer::parseInt)
                     .toArray();
    }

    @Test
    public void testInsertionSort() {
        int[] arrCopy = arr.clone();
        lab2.insertionSort(arrCopy);
        assertArrayEquals(corAns, arrCopy);
    }

    @Test
    public void testMergeSort() {
        int[] arrCopy = arr.clone();
        lab2.mergeSort(arrCopy);
        assertArrayEquals(corAns, arrCopy);
    }

    @Test
    public void testFindMax() {
        int maxElement = lab2.findMax(arr, 0, arr.length - 1);
        assertEquals(maxElement, Arrays.stream(arr).max().orElseThrow());
    }

    @Test
    public void testBinarySearch() {
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);
        int resultIndex = lab2.binarySearch(sortedArr, 0, sortedArr.length - 1, target);
        int expectedIndex = Arrays.binarySearch(sortedArr, target);
        assertEquals(resultIndex, expectedIndex);
    }
}