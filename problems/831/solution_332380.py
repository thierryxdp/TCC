def lingua_p(palavra):
    """Função que dada uma palavra (em português), retorna
    esta mesma palavra traduzida na 'língua do P';
    str -> str"""
    vogais = 'aeiouáéíóú'
    traducao = ''
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in vogais:
            traducao = traducao + letra + 'p' + letra
        else:
            traducao = traducao + letra
    return traducao