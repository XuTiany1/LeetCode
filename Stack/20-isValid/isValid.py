class Solution:
    def isValid(self, s: str) -> bool:

        parantheses_brackets = {')': '(' ,
                                ']': '[' ,
                                '}': '{' 
                                }
        
        stack = []

        for curr_char in s:

            if curr_char in parantheses_brackets:

                top_ele = stack.pop()

                if top_ele != parantheses_brackets[curr_char]:

                    return False
                
            else:
                
                stack.append(curr_char)


            
        if len(stack) == 0:
            return True
        else:
            return False











