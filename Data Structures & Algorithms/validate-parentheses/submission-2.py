class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        brkt_map =  { ")" : "(", 
                      "]" : "[", 
                      "}" : "{" }
        chars = []
        for i in s:
            if i in brkt_map:
                if chars and chars[-1] == brkt_map[i]:
                    chars.pop()
                else: 
                    return False
            else:
                chars.append(i)
        if chars: 
            return False 
        else:
            return True

            