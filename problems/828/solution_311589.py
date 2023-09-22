def primo(n):
    '''Retorna True caso o número n seja primo ou False caso não seja;
    int -> bool'''
    lista = []
    for i in range(1,n+1):
        if n%i == 0:
            list.append(lista, i)
            
        i = i+1

    if len(lista) > 2:
        return True

    else:
        return False