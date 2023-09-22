#Start your python function here
def filtra_pares(nums):
    '''Dada uma tupla com 4 números inteiros restorna uma nova tupla com apenas os números pares
    tuple(int,int,int,int) -> tuple(int,)'''
	tupla = ()
    if nums[0]%2 == 0:
        tupla+= (nums[0],)
    elif nums[1]%2 == 0:
        tupla+= (nums[1],)
    elif nums[2]%2 == 0:
        tupla+= (nums[2],)
    elif nums[3]%2 == 0:
        tupla+= (nums[3],)
    return tupla