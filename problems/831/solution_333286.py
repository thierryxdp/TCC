def lingua_p(palavra):
    vogais = ('a','á','à','ã','â','e','é','è','ê','i','í','ì','o','ó','ò','õ','ô','u','ú','ù','û')
    texto = str(palavra)
    for i in range(len(vogais)):
        if vogais[i] in palavra:
            txtp = str(vogais[i])+'p'+str(vogais[i])
            texto = str.replace(palavra, vogais[i], txtp)
    return texto