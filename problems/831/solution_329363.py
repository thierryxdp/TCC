def lingua_p(palavra):
    vogais = 'aeiouáéíóú'
    nova_palavra=palavra.lower()
    for el in nova_palavra:
        if el in vogais:
            nova_palavra = nova_palavra.replace(el,el+'p'+el)
    return nova_palavra