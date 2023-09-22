def lingua_p(palavra):
    
    """Retorna a palavra dada como entrada na lingua do P;
    str -> str
    """

    nova_palavra = ''

    for letra in palavra:
        if letra not in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            nova_palavra = nova_palavra + letra
        if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            nova_palavra = nova_palavra + letra + 'p' + letra
    return nova_palavra