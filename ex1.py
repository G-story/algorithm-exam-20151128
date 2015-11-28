import time

import factory


def solution(A):
    pass


start = time.time()
# print(solution([1]))
print(solution(factory.get('random').get_list(size=100000, min=-1000000, max=1000000)))
end = time.time()
print end - start
