def primo(n):
    lista = list(range(2,n))
    i = 0
    while i < len(lista):
        if n%lista[i] == 0:
            return False
        else:
            return True 
    return lista