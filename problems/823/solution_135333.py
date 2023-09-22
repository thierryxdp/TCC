def faltante(lista):
    somaPA=0
    i=0
    while i<(len(lista)+1):
        somaPA = somaPA + (1+i)
        i=i+1
    
    return somaPA-sum(lista)