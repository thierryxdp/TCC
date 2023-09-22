def conta_numero(n:int,lista:list)->int:
    """Calcula e retorna quantas vezes um número n inteiro 
       aparece na matriz dada"""
    
    i=0
    y=len(lista)
    contador=0
    
    while i<y:
        contador+=lista[i].count(n)
        i+=1
    return contador