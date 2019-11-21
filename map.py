"""
Map会将一个函数映射到一个输入列表的所有元素上。
规范：
map(function_to_apply, list_of_inputs)
"""

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)

# 可以进化为
def func_squared(x):
    return x**2
squared_pre = list(map(func_squared, items))
print(squared_pre)

# 或者
squared_pre_1 = list(map(lambda x:x**2, items))
print(squared_pre_1)