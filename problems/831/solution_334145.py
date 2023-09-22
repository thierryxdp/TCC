def lingua_p(palavra):
    """
    funcao que recebe uma palavra como parâmetro (em português) e retorna a
    palavra adicionando uma letra p antes das vogais
    :param palavra: str 
    :return: str 
    """
    minusculo = palavra.lower()
    palavrap = ''
    vogais = 'aeiouãáéíóú'
    for p in minusculo:
        palavrap += p
        if p in vogais:
            palavrap += 'p' + p

    return palavrap