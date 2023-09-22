def lingua_p(palavra):
    """Função que receba uma palavra em português e retorne essa palavra
    traduzida para a língua do P.
    str -> str"""
    vogais = ['a', 'e', 'i', 'o', 'u', 'á','à','â','ã','é','ê','í','ó','ô','õ','ú','ü']
    linguagem_p = []
    for letra in palavra:
        if letra in vogais:
            list.append(palavra, letra)
            list.append(palavra, 'p')
            list.append(palavra, letra)
        else:
            list.append(palavra, letra)
    return str.lower(str.join('',linguagem_p))