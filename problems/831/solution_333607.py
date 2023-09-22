def lingua_p(palavra):
    palavra = palavra.lower()
    vogais = ('a', 'e', 'i', 'o', 'u')

    for i in vogais:
        if(i in palavra):
            palavra = palavra.replace(i, i + 'p' + i)
        
    return palavra