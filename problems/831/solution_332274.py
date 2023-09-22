def lingua_p(palavra):
    for letra in palavra:
        if letra in 'aeiouAEIOU':
        	palavra = str.lower(palavra[:palavra.index(letra)+1] + 'p' + palavra[palavra.index(letra):])
    return palavra