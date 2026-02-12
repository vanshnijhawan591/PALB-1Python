class Solution {
  public:
    void reverseArray(vector<int> &arr) {
        int start = 0;
        int end = arr.size() - 1;

        while (start < end) {
            // Swap elements
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }
    }
};
