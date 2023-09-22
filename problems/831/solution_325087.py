def lingua_p(palavra):
    palavra = str.lower(palavra)
    vogais = 'aáàãeéèêiíoóôõuúü'
    traduzida = ''
    for c in palavra:
        traduzida = traduzida + c
        if c in 'aeiouáàãâéêíóôõú':
            traduzida = traduzida + 'p' + c
    return traduzida