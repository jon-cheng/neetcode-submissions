class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(',
                '}':'{',
                ']':'['}

        # scan the string left to right, looking for brackets
        # pushes and pops must happen in the correct order

        stack = []
        for char in s:
            # if left bracket: push
            if char in '({[':
                stack.append(char)
            else:
            # if right bracket: pop
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()

        # at the end of iteration, stack should be back to an empty list, having an equal of pop operations as enter

        return len(stack)==0