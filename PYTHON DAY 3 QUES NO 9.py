class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        import re
        pattern = re.compile("^" + p + "$")
        if pattern.search(s) is None:
            return False
        return True
S=input ("enter the ") 
P=input("enter the word")
