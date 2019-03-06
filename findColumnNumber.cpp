class Solution {
public:
    int titleToNumber(string s) {
        int total = 0;
        int n = s.size();
        for(int i = 0; i < n; i++){
            total += (s[i] - 'A' + 1)* pow(26, n - 1 - i);
        }
    return total;
    }
};
