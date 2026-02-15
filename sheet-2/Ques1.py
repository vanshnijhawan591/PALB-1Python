class Solution {
  public:
    int kthSmallest(vector<int> &arr, int k) {
        
        sort(arr.begin(), arr.end());
        
        return arr[k - 1];   // k-1 because indexing starts from 0
    }
};
