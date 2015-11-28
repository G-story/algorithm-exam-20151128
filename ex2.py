import time


def a(part, target_sum, cur_sum):
    idxs = []
    for i in xrange(len(part)):
        if cur_sum + part[i] == target_sum:
            return i
        ret = a(part[i + 1:], target_sum, cur_sum + part[i])
        if ret > 0:
            idxs += ret
            idxs.append(i)
            return idxs
    return []


def solution(A):
    if sum(A) % 3 != 0:
        return "impossible"
    avg_num = sum(A) / 3
    rgb = len(A) * ["R"]
    for color in xrange(3):
        idxs = a(A, avg_num, 0)
        for i in xrange(len(idxs)):
            if color == 0:
                rgb[idxs[i]] = "R"
            elif color == 1:
                rgb[idxs[i]] = "G"
            else:
                rgb[idxs[i]] = "B"
    return ''.join(rgb)





start = time.time()
print(solution([3, 7, 2, 5, 4]))
# print(solution(factory.get('random').get_list(size=100000, min=-1000000, max=1000000)))
end = time.time()
print end - start
