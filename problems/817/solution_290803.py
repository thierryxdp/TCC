def maiores(numeros,n):
    """a função ordena a lista, encontra o indice do número e retorna os valores maiores.
    Entradas lista, int e saida lista"""
    list.append(numeros, n)
    list.sort(numeros)
    x = list.index(numeros, n)
    list.remove(numeros, n)
    return numeros[x:]

def acima_da_media(notas):
    """Essa função determina a media das notas e retorna as notas que estão acima da mesma.
    Entrada lista e saida lista"""
    y = sum(notas)/len(notas)
    
    if int(y) in maiores(notas,y):
        return maiores(notas,y)[1:]
    
    else:
        return maiores(notas,y)