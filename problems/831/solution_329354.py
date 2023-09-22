def lingua_p(palavra):
    vogais = 'aeiouáéíóú'
    nova_palavra = palavra.lower()
    for i in range(len(nova_palavra)):
        if nova_palavra[i] in vogais:
            nova_palavra=nova_palavra.replace(nova_palavra[i],nova_palavra[i]+'p'+nova_palavra[i])
    return nova_palavra