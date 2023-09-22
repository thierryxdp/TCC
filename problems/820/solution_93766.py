def posLetra(texto:str, letra:str, ocorrencia:int) -> int:
    """Função retorna a posição da ocorrência desejada da letra no texto fornecido
       
       Parameters:
       texto: texto analisado
       letra: letra a ser encontrada
       ocorrencia: ocorrencia desejada da letra
       
       Returns:
       posição da letra na ocorrencia desejada
    """
    posicoes = []
    i = 0
    
    while i < len(texto):
        if str.upper(texto[i]) in str.upper(letra):
            posicoes += [i]
        i = i + 1
        if len(posicoes) < ocorrencia:
            return -1
    return posicoes[ocorrencia -1]