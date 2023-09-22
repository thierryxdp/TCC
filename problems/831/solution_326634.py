def lingua_p(palavra):
    for i in palavra:
        vogais = 'AEIOUaeiou'
        if i in vogais:
            palavra = palavra.replace(i,i+"p")
        else: i=+1
    return palavra