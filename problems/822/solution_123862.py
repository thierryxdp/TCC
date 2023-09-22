def repetidos(nums):
    '''retorna quantos numeros sao iguais ao anterior;
    list->int'''
    i=1
    reps=[]
    while i<len(nums):
        if nums[i]==nums[i-1]:
        	list.append(reps,'um')
        i=i+1
    return len(reps)