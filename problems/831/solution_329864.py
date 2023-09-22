def lingua_p(palavra):
    """
    Função que adiciona uma letra p antes da vogal de uma dada palavra.
    str -> str
    """
    palavra_minusculo = palavra.lower()
    nova_palavra = ''
    vogais = 'aeiouãáéíóú'
    for p in palavra_minusculo:
        nova_palavra += p
        if p in vogais:
            nova_palavra += 'p' + p

    return nova_palavra