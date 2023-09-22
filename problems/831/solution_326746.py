def lingua_p(palavra):
    """Funcaona qual retorna a palavra na lingua do P"""
    vogais = ['a','á','à','ã','â','e','é','é','ê','i','í','ì','î','o','ó','ò','ô','õ','u','ú','ù','û']
    resposta = []
    for letra in palavra:
        if letra in vogais:
            aux = letra + "p" + letra
            list.append(resposta,aux)
        else:
            list.append(resposta,letra)   
    return str.join("",resposta)