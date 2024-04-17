class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dics1 = {}
        dics2 = {}
        
        for char in s1:
            if char not in dics1:
                dics1[char] = 0
            dics1[char]+=1
            
        start = 0
        
        for end, char in enumerate(s2):
            if char not in dics2:
                dics2[char]=0
            dics2[char]+=1
            
            size = end-start+1
            
            if size==len(s1):
                if dics1==dics2:
                    return True
            
                if dics2[s2[start]]==1:
                    del dics2[s2[start]]
                else:
                    dics2[s2[start]]-=1
                    
                start+=1
        return False
                
                