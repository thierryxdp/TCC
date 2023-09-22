def lingua_p(palavra):
    """
    	Recebe uma palavra na língua portuguesa e retorna
        a palavra traduzida para língua do P.
    """
    vogais = 'aeiouAEIOU'
    palavraRepartida = []
    indexs = []
    traducao = ""
    for letra in palavra:
        palavraRepartida += letra
    
    for letra in palavraRepartida:
        if letra in vogais:
            indexs += [list.index(palavraRepartida, letra)]

    for i in indexs:
        list.insert(palavraRepartida, i + 1, "p" + palavraRepartida[i])

    for letras in palavraRepartida:
        traducao += letras
        
    str.lower(traducao)
    
    return traducao