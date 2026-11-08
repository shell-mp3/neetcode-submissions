class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #start with empty string
        for s in strs: #loop through each string in list of strings
            res += str(len(s)) + "#" + s # add the length of string, plus delimeter, plus string 
        return res 

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # create empty list and set pointer to 0, i tracks where next word begins 

        while i < len(s):
            j = i
            while s[j] != "#": #j searches for the # operator 
                j += 1 #increase position 
            length = int(s[i:j]) #gets length of word before dilimeter 

            res.append(s[j+1 : j + 1 + length]) #next word 
            i = j + 1 + length #move i to the next word 
        return res    
