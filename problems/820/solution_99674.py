def posLetra(frase,letra,n):
    """ Recebe uma string, uma letra e um numero de entrada, retornanado a posição da letra na determinada ocorrencia;
    string->int """
    i=0
    string2=[]
    if frase.count(letra)<n:
        return -1
    while i<len(frase):
        if frase[i]==letra:
            string2=string2+[i]
        i=i+1
    return string2[n-1]