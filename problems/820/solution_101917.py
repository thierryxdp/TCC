def posLetra(frase,letra,n):
    """ Recebe uma frase, uma letra e um numero n de entrada, retornanado a posição da letra na determinada ocorrencia(n);
    string,strig,int->int """
    i=0
    lista=[]
    if frase.count(letra)<n:
        return -1
    while i<len(frase):
        if frase[i]==letra:
            lista=lista+[i]
        i=i+1
    return lista[n-1]