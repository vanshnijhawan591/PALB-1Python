class Solution {
  public:
    int minJumps(vector<int>& arr) {
        
        int n = arr.size();
        
        // If array has only one element
        if(n == 1) return 0;
        
        // If first element is 0, cannot move
        if(arr[0] == 0) return -1;
        
        int jumps = 1;            // At least one jump
        int maxReach = arr[0];    // Maximum reachable index
        int steps = arr[0];       // Steps we can still take
        
        for(int i = 1; i < n; i++) {
            
            // If we reached the last index
            if(i == n - 1)
                return jumps;
            
            // Update maximum reach
            maxReach = max(maxReach, i + arr[i]);
            
            steps--;  // Use one step
            
            // If no steps left
            if(steps == 0) {
                jumps++;
                
                // If current index is beyond maxReach
                if(i >= maxReach)
                    return -1;
                
                steps = maxReach - i;
            }
        }
        
        return -1;
    }
};
