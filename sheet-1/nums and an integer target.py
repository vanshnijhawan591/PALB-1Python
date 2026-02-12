class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> mp;  // value → index
        
        for(int i = 0; i < nums.size(); i++) {
            
            int complement = target - nums[i];
            
            // If complement already exists
            if(mp.find(complement) != mp.end()) {
                return {mp[complement], i};
            }
            
            // Store current value with index
            mp[nums[i]] = i;
        }
        
        return {};  // (Problem guarantees one solution)
    }
};
