def lingua_p(palavra):
    """Função que receba uma palavra em português e retorne essa palavra
    traduzida para a língua do P.
    str -> str"""
    vogais = ['a', 'e', 'i', 'o', 'u', 'á','à','â','ã','é','ê','í','ó','ô','õ','ú','ü']
    linguaDoP = []
    for letra in palavra:
        if letra in vogais:
            list.append(linguaDoP, letra)
            list.append(linguaDoP, 'p')
            list.append(linguaDoP, letra)
        else:
            list.append(linguaDoP, letra)
    return str.lower(str.join('',linguaDoP))