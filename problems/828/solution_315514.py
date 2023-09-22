def primo(num):
    lista_de_divisores=[]
    for el in range(1,num):
        if num%el==0:
            lista_de_divisores.append(el)
    if len(lista_de_divisores)>2:
        return False
    else:
        return True