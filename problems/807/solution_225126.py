def conta_frases(texto):
    digito1 = str.count(texto, '.')
    digito2 = str.count(texto, '!')
    digito3 = str.count(texto, '?')
    digito4 = str.count(texto, '...')
    if int(digito4) == 1:
        return int(digito1)+int(digito2)+int(digito3)+int(digito4)-(3)
    elif int(digito4) == 2:
        return int(digito1)+int(digito2)+int(digito3)+int(digito4)-(6)
    else:
        return int(digito1)+int(digito2)+int(digito3)