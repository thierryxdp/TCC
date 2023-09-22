def posLetra (string,letra,n):
    """retorna em que posição da string aquela ocorrência da letra está, caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1"""
    posicao=0
    repeticao=0
    while letra in string:
        if repeticao<n:
            posicao=str.find(string,letra)
            string=string[posicao+1]
            posicao=posicao+1
            repeticao=repeticao+1
            return repeticao
        else:
            return -1