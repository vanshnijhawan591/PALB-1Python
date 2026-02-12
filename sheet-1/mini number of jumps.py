class Solution {
  public:
    int minJumps(vector<int>& arr) {
        
        int n = arr.size();
        
        // If first element is 0, can't move
        if(arr[0] == 0) return -1;
        
        int jumps = 1;              // At least one jump needed
        int maxReach = arr[0];      // Maximum index we can reach
        int steps = arr[0];         // Steps we can still take
        
        for(int i = 1; i < n; i++) {
            
            // If we reached last index
            if(i == n - 1)
                return jumps;
            
            // Update maximum reach
            maxReach = max(maxReach, i + arr[i]);
            
            steps--;  // Use one step
            
            // If no more steps left
            if(steps == 0) {
                jumps++;
                
                // If current index is beyond max reach
                if(i >= maxReach)
                    return -1;
                
                steps = maxReach - i;
            }
        }
        
        return -1;
    }
};
