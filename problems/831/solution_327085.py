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
    minusculas = str.lower(palavra)
    palavra_P= ''
    indice = 0
    for i in range(len(minusculas)):
        if i in 'aeiou':
            palavra_P = palavra_P + minusculas[indice:i+1]+'p'+ minusculas[i]
            indice = i+1
    if indice != len(minusculas):
        palavra_P = pavalra_p + minusculas[indice:len(minusculas)]
    return palavra_P