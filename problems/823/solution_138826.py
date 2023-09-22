def faltante(lista):
    '''essa funçao recebe uma lista com N-1 numeros e precisa retornar qual o numero que esta
    faltando
    lista-> int'''
    i=0
    list.sort(lista)
    
    if lista[0]!=1:
        return 1
    else:
        while i < len(lista):
            if lista[i]!= lista[i-1]+1:
                x=lista[i-1]+1
            i=i+1
        return x