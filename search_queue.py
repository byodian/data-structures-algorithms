from collections import deque
# 建立图结构
graphy = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy', 'you'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': [],
}

def person_is_seller(name):
    return name[-1] == 'm'

# 使用广度优先搜索，在你的人际关系网中，计算找到 mogo 开发商的最短路径
# 使用散列表构建图结构
# 使用队列
def search(name):
    search_queue = deque()
    search_queue += graphy[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        # 防止无限循环的冲突，比如 you -> alice alice -> you
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True 
            else:
                search_queue += graphy[person]
                searched.append(person)

    print('No one is a mango seller!')
    return False

print(search('you'))
