class Solution {
  public:
    int getMinDiff(vector<int> &arr, int k) {
        
        int n = arr.size();
        if(n == 1) return 0;
        
        sort(arr.begin(), arr.end());
        
        int ans = arr[n-1] - arr[0];   // initial difference
        
        int smallest = arr[0] + k;
        int largest  = arr[n-1] - k;
        
        for(int i = 0; i < n-1; i++) {
            
            int mini = min(smallest, arr[i+1] - k);
            int maxi = max(largest, arr[i] + k);
            
            if(mini < 0) continue;   // skip negative heights
            
            ans = min(ans, maxi - mini);
        }
        
        return ans;
    }
};
