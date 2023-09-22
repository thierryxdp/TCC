def posLetra(string,letra,numero):
    """retorna em que posição da string a ocorrência da letra está
    caso não alcance a ocorrência pedida retorna -1;
    string, string, int -> int"""
    
    contar = 0
    posicao = 0
    while posicao < len(string):
        if letra==string[posicao]:
            contar+=1
            if contar==numero:
                return posicao
        posicao+=1
    return -1