def qtd_divisores(num):
    L=[]
    for i in range(1,num//2+2):
        if num%i==0:
            list.append(L,i)
    return len(L)