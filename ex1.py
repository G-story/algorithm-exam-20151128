import time

sparse_nums = [0, 1, 2]


def is_sparse(n):
    bin_n = "{0:b}".format(n)
    bin_len = len(bin_n)
    for i in xrange(bin_len - 1):
        if bin_n[i] == '1' and bin_n[i + 1] == '1':
            return False
    return True


def solution(N):
    n = 4
    while n <= N / 2 + 1:
        sparse_nums.append(n)
        bin_n = "{0:b}".format(n)
        len_s = len(sparse_nums)
        for i in xrange(len_s):
            new_n = int(bin_n, 2) + sparse_nums[i]
            if new_n >= N or new_n >= n + (n >> 1):
                break
            sparse_nums.append(new_n)
        n = n << 1

    for i in xrange(len(sparse_nums)):
        if is_sparse(N - sparse_nums[i]):
            return sparse_nums[i]
    return -1


start = time.time()
for i in xrange(0, 1000):
    print(i, solution(i) if solution(i) == -1 else None)
# print(solution(0))
# print(solution(factory.get('random').get_list(size=100000, min=-1000000, max=1000000)))
end = time.time()
print end - start

# "{0:b}".format(10)
# bin(10)
# int('11111111', 2)
