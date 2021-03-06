class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length())
            return false;
    
    int n = s.length();
    unordered_map<char, int> map;
    for(int i = 0; i < n; i++){
        map[s[i]]++;
        map[t[i]]--;
    }
        for(auto m : map)
            if (m.second) return false;
        return true;
    }
};
