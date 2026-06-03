class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #initialize pointer
        k = arr[-1]

        #loop through list backwards
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > k:
                temp = arr[i]
                arr[i] = k
                k = temp
            elif arr[i] < k:
                arr[i] = k
            
        arr[-1] = -1
        return arr