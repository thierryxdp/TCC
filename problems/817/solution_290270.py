def acima_da_media(notas):
    """Funcao que analisa as notas de uma turma, e retorna todas 
    as notas que ficaram acima da média. 
    Entrada: list;
    Saída: list;
    
    Parameters:
    notas: Lista de notas da turma.
    """
    media_notas = sum(notas) / len(notas)
    
    if media_notas in notas:
        notas.sort()
        posicao = notas.index(media_notas)
        return notas[posicao+1:]
    else:
        notas.append(media_notas)
        notas.sort()
        posicao = notas.index(media_notas)
        return notas[posicao+1:]