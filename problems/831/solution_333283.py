def lingua_p(palavra):
    vogais = ('a','e','i','o','u')
    texto = str(palavra)
    for i in range(len(vogais)):
        if vogais[i] in palavra:
            txtp = str(vogais[i])+'p'+str(vogais[i])
            texto = str.replace(palavra, vogais[i], txtp)
    return texto