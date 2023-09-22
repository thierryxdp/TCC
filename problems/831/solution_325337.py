def lingua_p(palavra):
    
    """Retorna a palavra dada como entrada na lingua do P;
    str -> str
    """

    nova_palavra = ''

    for letra in palavra:
        if letra not in 'aeiouAEIOU':
            nova_palavra = nova_palavra + letra
        if letra in 'aeiouAEIOU':
            nova_palavra = nova_palavra + letra + 'p' + letra
    return nova_palavra