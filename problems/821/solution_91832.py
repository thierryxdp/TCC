def fatorial(n):
    '''Dado um número n retorna seu fatorial
    int -> int'''
    nums = list(range(n,0,-1))
    fat = 1
    c = 0
    while c < len(nums):
        fat *= nums[c]
        c += 1

    return fat