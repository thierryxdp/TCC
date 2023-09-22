def primo(n):
    '''funcao que recebe um numero inteiro positivo e retorna
       um booleano, True se ele for primo e False caso ele 
       nao seja primo'''
    i= 0
    lista= []
    for x in range(n):
        if n%(i+1) == 0:
            list.append(lista,i+1)
        i += 1
    if len(lista) != 2:
        return False
    else:
        return True