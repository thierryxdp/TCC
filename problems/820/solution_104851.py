def posLetra(string,letra,n):
    """Função que retorna a posição de uma letra, dado o indice que ela se encontra. str, str, int -> int"""
    p= string.find(letra)
    while p>=0 and n>1:
        p= string.find(letra,p+1)
        n-=1
    return p