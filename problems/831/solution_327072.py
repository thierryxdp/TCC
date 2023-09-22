def lingua_p(palavra):
    """Função que recebe uma palavra em português e a traduz para a 
    língua do P.
    
    Observação: Uma palavra é traduzida para a língua do P quando após
    cada vogal da palavra original, é inserida a sequência: P + vogal
    original.
    
    Parameters:
    palavra: É a palavra escolhida para ser traduzida para a língua do P
    
    Returns:
    Retorna a tradução da palavrs para a língua do P.
    str -> str
    """
    str.lower(palavra)
    for vogal in len(palavra):
        if vogal == "aeiou":
            P=str.join('p'vogal,palavra)
    return P