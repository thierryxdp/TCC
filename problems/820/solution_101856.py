def posLetra(string,letra,n):
    '''Recebe uma string, uma letra e um numero e e retorna a posição da ocorrencia n da letra na string
    str,str,int -> int'''
    if frase.count(letra)<n:
        return -1
    i=0
    letras=[]
    while i<len(string) and len(letras)<n:
        if letra == string[i]:
            list.append(letras,string[i])
        i=i+1
    return i-1