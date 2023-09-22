def primo(n):
    '''Ao fornecer um numero inteiro, verifica se esse número é um primo.

    int -> bool'''

    lista = []
    for numero in range(2,n+1):
        if n%numero == 0:
            list.append(lista,numero)

    if len(lista)>1:
        return False
        
    else:
        return True