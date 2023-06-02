def quickSort(low,high,nums):
    if(low<high):
        pI=partition(low,high,nums)
        quickSort(low,pI-1,nums)
        quickSort(pI+1,high,nums)



def partition(low,high,nums):

    pivot=nums[low]

    i=low;
    j=high;

    while i < j:
        while i<=high and nums[i]<=pivot:
            i+=1
        while j>=low and nums[j]>pivot:
            j-=1
        if i<j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp


    temp=nums[low]
    nums[low]=nums[j]
    nums[j]=temp

    print(nums,j)

    return j




lst=[5,4,3,2,1]

quickSort(0,len(lst)-1,lst)

print(lst)
print(lst)
print(lst)

