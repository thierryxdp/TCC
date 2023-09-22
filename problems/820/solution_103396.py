def posLetra(frase, letra, n):
    '''retorna a posicao da ocorrencia n da letra na frase
    str, str, int-> int'''
    posicao=0
    while n<len(frase):
        if str.count(frase, letra)<n:
            return -1
        if n==1:
            return str.find(frase, letra, 1)
        if letra in frase[n]:
            posicao=posicao+1
        return str.find(frase, letra, n)