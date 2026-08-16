import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = collections.defaultdict(int)
        dict_t = collections.defaultdict(int)

        for letter in s:
            dict_s[letter] += 1
        for letter in t:
            dict_t[letter] += 1

        for letter in s:
            if dict_s[letter] != dict_t[letter]:
                return False
        for letter in t:
            if dict_t[letter] != dict_s[letter]:
                return False
        
        return True
                