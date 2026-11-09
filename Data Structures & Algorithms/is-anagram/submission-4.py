class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag_dict = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in anag_dict:
                anag_dict[s[i]] = 1
            else:
                anag_dict[s[i]] += 1

        for i in range(len(s)):
            if t[i] in anag_dict:
                anag_dict[t[i]] -= 1
                if anag_dict[t[i]] == 0:
                    del anag_dict[t[i]]
            else:
                return False
        
        if anag_dict:
            return False
        else:
            return True