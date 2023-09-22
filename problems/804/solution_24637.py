#Start your python function here
def filtra_pares(nums):
    """Retorna uma tupla contendo apenas os números pares presentes na tupla de entrada.
    tuple -> tuple"""
    pares = list(nums)
    if nums[0] % 2 == 1:
        pares.remove(nums[0])
    if nums[1] % 2 == 1:
        pares.remove(nums[1])
    if nums[2] % 2 == 1:
        pares.remove(nums[2])
    if nums[3] % 2 == 1:
        pares.remove(nums[3])
    return tuple(pares)