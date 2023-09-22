def lingua_p(palavra):
    """
    funcao que recebe uma palavra como parâmetro (em português) e retorna a
    palavra adicionando uma letra p antecedendo as vogais
    str--->str
    """
    
    palavrap = ''
    vogais = 'aeiouãáéíóú'
    letraminuscula = palavra.lower()
    for p in letraminuscula:
        palavrap += p
        if p in vogais:
            palavrap += 'p' + p

    return palavrap