# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'miniMaxSum' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #

# def miniMaxSum(arr):
#     # Write your code here
#     arr.sort()
#     minArr = arr[:-1]
#     maxArr = arr[1:]
#     minSum = maxSum = 0
#     for i in range(len(minArr)):
#         minSum += minArr[i]
#     for j in range(len(maxArr)):
#         maxSum += maxArr[j]    
#     print(minSum, maxSum)
    
# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minArr = arr[:-1]
    maxArr = arr[1:]
    sumArr = [0, 0]
    for i in range(len(minArr)):
        sumArr[0] += minArr[i]
        sumArr[1] += maxArr[i]
    print(sumArr[0], sumArr[1])
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

