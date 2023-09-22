def acima_da_media(nota):
    """Funcao calcula e retorna as notas acima da media """
    media=sum(nota)/len(nota)
    resultado=maiores(nota,media)
    

def maiores(lista,n):
    """funcao calcula e retirno uma lista original(lista) com seus elementos maiores que um numero inteiro(n).
    int,int-->int"""
    lista.append(n)
    lista.index(n)
    lista.sort()
    ind=lista.index(n)
    return lista[ind+1:]