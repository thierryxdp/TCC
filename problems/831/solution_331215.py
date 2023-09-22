def lingua_p(palavra):
    """Adiciona uma letra p antes da vogal de uma dada palavra."""
    palavra = str.lower(palavra)
    palavra_nova = ''
    vogais = 'aeiouãáâéíóúõô'
    for i in palavra:
        palavra_nova = palavra_nova + i
        if i in vogais:
            palavra_nova = palavra_nova + 'p' + i

    return palavra_nova