def filtraMultiplos(nums, n):
    cont=0
    numeros = []
    while cont<len(nums):
        if nums[cont] % n == 0:
            numeros = numeros + [nums[cont]]
        cont = cont+1
    return numeros

            
filtraMultiplos([0,2,4,5,9,10,15], 3)

filtraMultiplos([0,2,4,5,9,10,15], 5)