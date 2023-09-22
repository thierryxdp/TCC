def lingua_p(word):
    palavra = list(word)
      resultado = ''
        resposta = ''
    vogais = 'AEIOU aeiou À Á Â Ä Å Ã Æ Ç É È Ê Ë Í Ì Î Ï Ñ Ó Ò Ô Ö Ø Õ Œ Ú Ù Û Ü Ý Ÿ Ŷ à á â ä å ã æ ç é è ê ë í ì î ï ñ ó ò ô ö ø õ œ ú ù û ü ý ÿ ŷ'
    i = 0
   
    while i <= len(palavra):
    if palavra[i] in vogais:
    resultado = palavra[i] + 'p' + (palavra[i].lower())

    else:
    resultado = palavra[i]

    i = i + 1
    resposta += resultado.lower()

    return resposta