def qtd_divisores(num):
    lista_divisores=[]
    for el in range(1,num+1):
        if num%el==0: 
           lista_divisores.append(el)
    return len(lista_divisores)