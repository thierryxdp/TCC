def primo(n):
    '''
    Funçao que verifica se um numero é primo
    int-> bool
    '''
    lista=[]
    if n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                list.append(lista,i)
                return False, lista
            else:
                list.append(lista,i)
                return True, lista