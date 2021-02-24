class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()#记录每个字母最后一次出现的下标,key是字母，val是下标
        res, start = 0, 0
        for end in range(len(s)):
            if s[end] in record:#出现过
                start = max(start, record[s[end]] + 1)
            record[s[end]] = end #刷新最新下标
            res = max(res, end - start + 1)  #刷新res
        return res

s="acvdfdffffghhjersadf"
C = Solution()
print(C.lengthOfLongestSubstring(s))
