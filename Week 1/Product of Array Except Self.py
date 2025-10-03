class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [0]*l
        post = [0]*l
        pre.append(1)
        pre.insert(0,1)
        post.append(1)
        post.insert(0,1)
        total = 0
        for i in range(l):
            pre[i+1] = nums[i] * pre[i]
        for i in range(l-1,-1,-1):
            post[i+1] = nums[i] * post[i+2]
        res = [0]*l
        for i in range(l):
            res[i] = pre[i] * post[i+2]
        return res
        

        


        
         
