#Start your python function here
def filtra_pares(nums):
    tupla=()
    if nums[0] % 2 == 0:
        tupla +=(nums[0],)
    if nums[1] % 2 == 0:
        tupla +=(nums[1],)
    if nums [2] % 2 == 0:
        tupla +=(nums[2],)
    if nums[3] % 2 == 0:
        tupla +=(nums[3],)
    else:
        return tupla