# Minimise-Distance
#给定一个数组 strs，其中的数据都是字符串，给定两个字符串 str1，str2。如果这两个字符串都在 strs数组中，就返回它们之间的最小距离；如果其中任何一个不在里面，则返回 -1；如果两个字符串相等，则返回 0。

# first solution

def min_distance_1(strs,str1,str2):

    if str1 not in strs or str2 not in strs:
        return -1
    if str1 == str2:
        return 0
    dist, min = 1, len(strs)
    pos1, pos2 = 0, len(strs)
    for i in range(0, len(strs)):
        if str1 == strs[i]:
            pos1 = i
            for j in range(0, len(strs)):
                if str2 == strs[j]:
                    pos2 = j
                dist = abs(pos1 - pos2)
                if dist < min:
                    min = dist
    return min
    
# Second solution

def min_distance_2(strs, str1, str2):

    if str1 not in strs or str2 not in strs:
        return -1
    if str1 == str2:
        return 0

    def creat_hash(strs):
        strs_set = list(set(strs))
        dist_hash = {}
        for i in range(0, len(strs_set)):
            temp = {}
            for j in range(0, len(strs_set)):
                if strs_set[i] != strs_set[j]:
                    dist = min_distance_1(strs,strs_set[i],strs_set[j])
                    temp[strs_set[j]] = dist
            dist_hash[strs_set[i]] = temp
        return dist_hash
    return creat_hash(strs)[str1][str2]

strs = ['*','3','*','5','10','9','7','1','*']
str1 = ['*']
str2 = ['9']


import time

tic = time.time()
distance1 = min_distance_1(strs,str1,str2)
toc = time.time()
print(distance1)
print("time1 = " + str(toc - tic))

tic = time.time()
distance2 = min_distance_2(strs,str1,str2)
toc = time.time()
print(distance2)
print("time2 = " + str(toc - tic))

————————————————
Result

-1
time1 = 5.245208740234375e-06
-1
time2 = 5.0067901611328125e-06

Process finished with exit code 0

