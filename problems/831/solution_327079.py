def lingua_p(palavra):
    """Função que recebe uma palavra em português e a traduz para a
    língua do P.
    
    Observação: Uma palavra é traduzia para a língua do P quando após
    cada vogal da palavra original, é inserida a sequência: p + vogal
    original.
    
    Parameters:
    palavra: É a palavra escolhida para ser traduzida para a língua do P.
    
    Returns:
    Retorna  tradução da palavra para a língua do P.
    str -> str
    """
    str.lower(palavra)
    P=''
    for vogal in palavra:
        if vogal in 'aeiou':
        P = str.join('p'+vogal,palavra)
    return P