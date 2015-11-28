import time


def is_sparse(n):
    bin_n = "{0:b}".format(n)
    bin_len = len(bin_n)
    for i in xrange(bin_len - 1):
        if bin_n[i] == '1' and bin_n[i + 1] == '1':
            return False
    return True


def solution(N):
    if N < 3:
        return -1
    for i in xrange(1, N / 2 + 1):
        if is_sparse(i) and is_sparse(N - i):
            return i
    return -1


start = time.time()
print(solution([1]))
# print(solution(factory.get('random').get_list(size=100000, min=-1000000, max=1000000)))
end = time.time()
print end - start
