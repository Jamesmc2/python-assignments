# def biggie_size(nums):
#     for x in range(0,len(nums)):
#         if nums[x]>0:
#             nums[x]='big'
#     return nums
# print(biggie_size([1,2,3,4,5,-1]))      

# def count_positives(nums):
#     y=0
#     for x in nums:
#         if x>0:
#             y+=1
#     nums[len(nums)-1]=y
#     return nums
# print(count_positives([-1,1,1,1]))    

# def sum_of_list(nums):
#     y=0
#     for x in nums:
#         y+=x
#     return y
# print(sum_of_list([1,2,3,4]))        

# def average(nums):
#     y=0
#     for x in nums:
#         y+=x
#     y=y/len(nums)
#     return y
# print(average([1,2,3,4]))    

# def length(nums):
#     y=0
#     for x in nums:
#         y+=1
#     return y
# print(length([1,2,3,4,5]))        

# def min(nums):
#     y=nums[0]
#     if len(nums)==0:
#         return False
#     for x in nums:
#         if x<y:
#             y=x
#     return y
# print(min([37,2,1,-9]))         

# def max(nums):
#     y=nums[0]
#     if len(nums)==0:
#         return False
#     for x in nums:
#         if x>y:
#             y=x
#     return y
# print(max([37,2,1,-9]))   

# def analysis(nums):
#     count=0
#     small=nums[0]
#     big=nums[0]
#     avg=0
#     final={}
#     for x in nums:
#         count+=x
#         if x>big:
#             big=x
#         if x<small:
#             small=x
#     final['sumTotal']=[count]
#     final['average']=[count/len(nums)]
#     final['minimum']=[small]
#     final['maximum']=[big]
#     final['length']=[len(nums)] 
#     return final
# print(analysis([37,2,1,-9]))           

# def reverse(values):
#     temp=0
#     for x in range(0,int(len(values)/2)):
#         temp=values[x]
#         values[x]=values[len(values)-(x+1)]
#         values[len(values)-(x+1)]=temp
#     return values
# print(reverse([37,2,1,-9,8]))        
