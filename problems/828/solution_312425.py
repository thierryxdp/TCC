def primo(numero):
    '''recebe um número inteiro e retorna True se o número for primo e False se não for.
    int -> bool'''
    lista = list(range(numero+1))
    pos = 0
    lista_divisores = []
    
    for elemento in lista:
        if n%(elemento+1) == 0:
            list.append(lista_divisores,numero/(elemento+1))
        pos = pos + 1
    if len(lista_divisores) == 2:
        return True
    else:
        return False