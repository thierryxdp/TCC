def lingua_p(palavra):
    vogais = ('a','e','i','u','o')
    texto = palavra
    for i in range(len(vogais)):
        if vogais[i] in palavra:
            txtp = str(vogais[i])+'p'+str(vogais[i])
            texto = palavra.strip(str(palavra), str(vogais[i]), txtp)
    return texto