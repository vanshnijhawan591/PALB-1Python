class Solution {
  public:
  
    void mergeArrays(vector<int>& a, vector<int>& b) {
        
        int n = a.size();
        int m = b.size();
        
        int gap = (n + m + 1) / 2;
        
        while(gap > 0) {
            
            int i = 0;
            int j = gap;
            
            while(j < n + m) {
                
                // Both in a
                if(i < n && j < n) {
                    if(a[i] > a[j])
                        swap(a[i], a[j]);
                }
                
                // i in a, j in b
                else if(i < n && j >= n) {
                    if(a[i] > b[j - n])
                        swap(a[i], b[j - n]);
                }
                
                // Both in b
                else {
                    if(b[i - n] > b[j - n])
                        swap(b[i - n], b[j - n]);
                }
                
                i++;
                j++;
            }
            
            if(gap == 1)
                gap = 0;
            else
                gap = (gap + 1) / 2;
        }
    }
};
