def posLetra(frase,l,n):
    """Função que recebe uma frase, uma letra e um número que indica a ocorrência desejada da letra e retorna em que posição aquela ocorrência da letra está
       Caso exita menos ocorrências da letra do que a ocorrêcia pedida a função deve retornar -1
       Parametros: str,str,int -> int"""
    posicao = 0
    contador = 0
    while posicao < len(frase):
        if frase[posicao] == l:
            contador = contador + 1
            if contador == n:
                return posicao
        posicao = posicao + 1
    else:
        return -1