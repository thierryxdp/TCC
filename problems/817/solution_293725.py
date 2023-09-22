def acima_da_media(nota):
    """Funcao calcula e retorna uma lista das notas acima da media;
    int,int-->int"""
    media=sum(nota)/len(nota)
    resultado=maiores(nota,media)
    return resultado

def maiores(lista,n):
    """funcao calcula e retirno uma lista original(lista) com seus elementos maiores que um numero inteiro(n).
    int,int-->int"""
    lista.append(n)
    lista.index(n)
    lista.sort()
    ind=lista.index(n)
    rep=lista.cound(n)
    return lista[ind+rep:]