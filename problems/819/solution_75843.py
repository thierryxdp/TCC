# Dada uma lista e um inteiro n, esta função retorna uma nova lista contendo
# todos os números da lista dada que são múltiplos de n.
# list , n -> list

def filtraMultiplos(lista,n):
    i=0
    resp = []
    
    while i<len(lista):
        if lista[i]%n ==0:
            resp = resp + [lista[i]]
        i = i+1
        
    return resp