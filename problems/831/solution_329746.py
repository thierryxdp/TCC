def lingua_p(palavra):
    """retorna a palavra em palavra em portugues traduzida para a lingua do P"""
    """str -> str"""
    
    traducao = ''
    str.lower(palavra)
    for letra in palavra:
        if letra in 'aáàâãeéèêiíìîoóòôõuúùû':
            letra_p = letra + 'p' + letra
            traducao += letra_p
        else:
            traducao += letra
    return traducao