def posLetra(frase,letra,n):
    '''Recebe uma frase, letra e numero e retorna o indice da ocorrencia n da letra informada na frase.
    str,str,int -> int'''
    i=frase.find(letra)
    while i>=0 and n>1:
        i = frase.find(letra,i+1)
        n = n-1
    return i