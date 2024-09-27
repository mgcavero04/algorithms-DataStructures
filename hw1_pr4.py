class Stack:
    def greater(nums1 , nums2): #For each 0 <= n < len(nums1), find the index m such that nums1[n] ==nums2[m] and determine the next greater element of nums2[m] in nums2. If there is no next greater element, then the answer for this query is -1. Return an array ans of length len(nums1) such that ans[n] is the next greater element as described above.
        stack=[]
        stackLength=len(nums2)
        
        for n in nums1 :
            next=0
            for m in nums2:
                if n == m and next<=stackLength-2:
                    nextNext = next+1
                    stackNext=nums2[nextNext]
                    if n<stackNext and next<=stackLength-2:
                        stack.append(stackNext)
                        
                    stack.append(-1)
                next +=1
        return stack
    
    def greaterImproved(nums1 , nums2): 
        nums1G = {}
        stack = []
        greater=[]
        for n2 in reversed(nums2):
            while stack and stack[-1] <= n2:
                stack.pop()
            if stack:
                nums1G[n2] = stack[-1]  
            else: 
                nums1G[n2]=-1
            stack.append(n2)
        for n in nums1:     
            greater.append(nums1G[n])
        return greater
        
   
    
def main(): 
        greater=[]
        substack=[]
        substack.append(4) 
        substack.append(1) 
        substack.append(2) 
        nums2=[]
        nums2.append(1)
        nums2.append(3)
        nums2.append(4)
        nums2.append(2)
 
        greater=Stack.greaterImproved(substack, nums2)
        print("greater:",greater)

if __name__ == "__main__":
        main()

