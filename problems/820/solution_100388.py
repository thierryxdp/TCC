def posLetra(palavra,letra, n):
    """Retorna a posicao da letra desejada conforme o valor de n;
    	str,str,int -> int"""
    posicao = palavra.find(letra)
    while posicao >= 0 and n > 1:
        posicao = palavra.find(letra, posicao + 1)
        n -= 1
    return posicao