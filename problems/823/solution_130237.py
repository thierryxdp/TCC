def faltante(lista):
    '''funcao que dada uma lista retorna o numero que falta
    para essa lista ficar com os numeros completos
    list->int'''
    i=0
    resultado=1
    while i<len(lista):
        x=list(range(1,lista[-1]+1))
        if x[i]==lista[i]:
            resultado+=1
        i=i+1
    return resultado