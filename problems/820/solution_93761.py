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
        if letra not in texto:
            return -1
        if str.upper(texto[i]) in str.upper(letra):
            posicoes += [i]
        i = i + 1
    return posicoes[ocorrencia -1]