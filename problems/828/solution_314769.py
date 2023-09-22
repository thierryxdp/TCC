def primo (numero):
    lista_divisores=numero
    for i in range(1,numero):
        if numero%i==0:
            list.append(lista_divisores,i)
    if len(lista_divisores)==2:
        return True
    elif len(lista_divisores)!=2:
        return False