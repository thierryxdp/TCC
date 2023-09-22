def lingua_p(palavra):
    ''''''
    traducao=''
    for letra in palavra:
        if str.lower(letra) not in 'bcdfghjklmnpqrstvwxyz':
            traducao+=letra+'p'+letra
        else:
            traducao+=letra
    return str.lower(traducao)