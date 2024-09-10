class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        dct = {}
        
        for word in strs:
            mod_word = "".join(sorted(word))
            dct.setdefault(mod_word, []).append(word)
        
        for key,value in dct.items():
            res.append(value)
            
        return res
