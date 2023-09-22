def lingua_p (palavra):
    ''''''
    palavratraduzida=''
    for letra in palavra:
        if str.lower(letra) not in 'bcdfghjklmnpqrstvwxyzç':
            palavratraduzida += letra + 'p' + letra
        else:
            palavratraduzida += letra
    return str.lower(palavratraduzida)