def qtd_divisores(numero):
    '''essa funçao conta quantos divisores um numero tem
    int->int'''
    lista= list(range(1, numero+1))
    lista_div=[]
    
    for elemento in lista:
        if numero%elemento==0:
            list.append(lista_div, elemento)
    return len(lista_div)