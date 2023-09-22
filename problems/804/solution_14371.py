def filtra_pares(nums):
    #Função que recebe uma tupla e filtra apenas os numeros pares
    #tuple -> tuple
    if nums[0] % 2 == 0:
        final = (nums[0],)
    if nums[1] % 2 == 0:
        final += (nums[1],)
    if nums[2] % 2 ==  0:
        final += (nums[2],)
    if nums[3] % 2 ==  0:
        final += (nums[3],)
        return final