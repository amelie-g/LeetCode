class Solution {
public:
    int firstUniqChar(string s) {
        int unique[256] = {0};
        for(auto i: s){
            unique[i]++;
        }   
        for(int i = 0; i < s.length(); i++){
            if (unique[s[i]] == 1)
                return i;
        }
        return -1;
    }
};
