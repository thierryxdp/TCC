def qtd_divisores(num)
    lista_divisores=''
    for el in range(1,num):
        if num%el==0:
            lista_divisores=lista_divisores+len(num)