class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = strs[0]
        
        for string in strs[1:]:
            while not string.startswith(commonPrefix):
                commonPrefix = commonPrefix[:-1]
            if not commonPrefix :
                return ""
        return commonPrefix
