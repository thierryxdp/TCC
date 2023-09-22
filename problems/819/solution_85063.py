def filtraMultiplos(nums,n):
    cont=0
    numero=[]
    while cont<len(nums):
        if nums[cont]%n==0:
            numero=numero+[nums[cont]]
        cont=cont+1   
    return numero