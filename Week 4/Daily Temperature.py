class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            val = 1
            for j in range(i + 1,len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    val = val + 1
                else:
                    res.insert(i,val)
                    break
        
        for i in range( (len(temperatures) - len(res))):
            res.append(0)

        return res

        
