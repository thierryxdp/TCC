def lingua_p (palavra):
    """Função que retorna uma palavra traduzida para a língua do P"""
    """string -> string"""
    P = ''
    for letra in palavra:
        P += letra
        if letra in 'aáãàâéêeíîioòõôúu':
            P += 'p'+letra
        return P