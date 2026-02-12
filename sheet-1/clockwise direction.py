class Solution {
  public:
    void rotate(vector<int> &arr) {
        
        int n = arr.size();
        
        int last = arr[n - 1];   // store last element
        
        // shift elements to right
        for(int i = n - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        
        arr[0] = last;   // put last element at first
    }
};
