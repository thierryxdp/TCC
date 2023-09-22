def posLetra(frase, letra, n):
    '''retorna a posicao da ocorrencia n da letra na frase
    str, str, int-> int'''
    posicao=0
    while n<len(frase):
        if n==1 and letra in frase:
            return 0
        if str.count(frase, letra)<n:
            return -1
        if letra in frase[n]:
            posicao=posicao+1
        return str.find(frase, letra, n)