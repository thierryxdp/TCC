def lingua_p(palavra):
    palavra_alterada = ''
    palavra = palavra.lower()
    for letra in palavra:
        if letra in 'aeiouáéíúóãõ':
            comP = letra + 'p' + letra
            palavra_alterada += comP
        else:
            palavra_alterada += letra
    return palavra_alterada