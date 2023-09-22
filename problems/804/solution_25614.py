def filtra_pares(nums):
    #dada uma tupla com 4 numeros inteiros, retorna uma nova tupla com apenas os numeros tuple (int, int,int, int) -> tuple(int)
    tupla= ()
    if nums[0]%2==0:
        tupla +=(nums[0],)
    if nums[1]%2==0:
        tupla +=(nums[1],)
    if nums[2]%2==0:
        tupla +=(nums[2],)
    if nums[3]%2==0:
        tupla +=(nums[3],)
    return tupla