"""
提示：
编写涉及数组的递归函数时，基线条件通常时数组为空或只 包含一个元素
"""

# 使用递归算法求数组的和
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

total = sum([1, 2, 3])
print(total) #6

#计算列表包含的元素个数
def count(list):
    if len(list) == 1:
        return 1
    return 1 + count(list[1:])

print(count([1, 2, 3])) #3

#列表中的最大值
def max(list):
    if len(list) == 1:
        return list[0]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max([1, 2, 3, 34]))
