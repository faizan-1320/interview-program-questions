# =============================================== Find Maximum Number ========================================
arr = [2,4,6,7,9,1,0,100,900]

# print(sorted(arr)[-2])

max_x = 0
second_max = 0

for i in arr:
    if i > max_x:
        second_max = max_x
        max_x = i
    elif i > second_max:
        second_max = i
print(second_max) 

# =============================================== Count the letter ========================================

s = 'aabbccaade'
count = 0
d = {}
for i in s:
    if i in d:
        d[i] += 1 
    else:
        d[i] = 1
print(d)
q=''
for i,j in d.items():
    q += i+str(j)
print(q)
# 'a4b2c2d1e1'

# =============================================== Flatten List ========================================

arr=[1, [2, 3, [4]], 5]
def flatten_list(data):
    output = []
    for i in data:
        if type(i) == list:
            output.extend(flatten_list(i))
        else:
            output.append(i)
    return output
print(flatten_list(arr))

# =============================================== Two Sum ========================================

l = [2,7,11,15]
target = 9
l1=[3,3,0]
target1 = 6
def two_sum(data,target):
    for i in range(len(data)):
        for j in range(1,len(data)):
            if data[i] + data[j] == target:
                return (i,j)
        
x= two_sum(l,target)
print(x)

# =============================================== Diagonal Difference ========================================

arr = [[1,2,3],[4,5,6],[7,8,9]]
def diagonalDifference(arr): 
    # Write your code here 
    Leftsum = 0 
    Rightsum = 0 
    n = len(arr) 
    for i in range(n): 
        Leftsum += arr[i][i] 
        Rightsum += arr[i][n-i-1] 
    return abs(Rightsum - Leftsum)

# =============================================== Staircase ========================================

def staircase(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = staircase(n - 1, memo) + staircase(n - 2, memo)
    return memo[n]

climbing = staircase(5)
print(climbing)

# =============================================== Merge Dicit ========================================

d1 = {'a':1,'b':7}
d2 = {'b':3,'c':4}

def merge(d1,d2):
    new_d = {}
    for i,j in d1.items():
        if i in d2:
            new_d[i] = j+j+1
        else:
            new_d.update(d1)
            new_d.update(d2)
    return new_d
print(merge(d1,d2))

# =============================================== Merge List ========================================

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

def merge(nums1,nums2):
    l = []
    for i in nums1:
        if i != 0:
            l.append(i)
    new = l + nums2
    new.sort()
    return new

print(merge(nums1,nums2))

# =============================================== Comman Dicit ========================================

def dict_comman(input_data, parent_key=''):
    comman_dict = {}
    for key, value in input_data.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            comman_dict.update(dict_comman(value, new_key))
        else:
            comman_dict[new_key] = value
    return comman_dict

input_data = {"a": {"b": {"c": 1}}, "d": 2}    
print(dict_comman(input_data))
# Output: {'a.b.c': 1, 'd': 2}

# =============================================== Flatten Dicit ========================================

def flatten_dict(inp, parent_key='', sep='.'):
    new_d = {}
    for key, value in inp.items():
        full_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            new_d.update(flatten_dict(value, full_key, sep))
        else:
            new_d[full_key] = value
    return new_d

input_data = {"a": {"b": {"c": 1}}, "d": 2}
result = flatten_dict(input_data)
print(result)

# =============================================== Find Missing Number ========================================

l = [1,2,3,4,5,6,7,8,9,11]

for i in range(1,max(l)+1):
    if i not in l:
        print(i)

# =============================================== Sequence of Number ========================================

nums = [100,1,200,2,3,4,5,6,7,8,9,10]

temp = 0
flag = True
counter = 1
output_list = []

for item in nums:
    if not temp:
        temp = item
        flag = True
    while flag:
        if temp + 1 in nums:    
            counter += 1
            temp += 1
        else:
            output_list.append(counter)
            temp = 0
            counter = 1
            flag = False

print(max(output_list))
print(output_list)

# =============================================== Count the vowel in a string ========================================

name = 'faizan'
d = {}
vowel = ['a','e','i','o','u']
for i in name:
    if i in vowel:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
print(d)

# =============================================== Prime Number ==========================================================

def prime_number(data):
    new_list = []
    if data < 2:
        return new_list
    
    for num in range(2, data):
        is_prime = True
        for i in range(2, int(num//2) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            new_list.append(num)
    return new_list

print(prime_number(10))

# =============================================== Most Frequent Character ==========================================================

input_s =  "aabbbccdeee"  
# Output: "b"
count={}
max_count=0
for i in input_s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
    if count[i] > max_count:
        max_count = count[i]
for i,j in count.items():
    if j == max_count:
        print(i)
        break

# =============================================== ###### ========================================
