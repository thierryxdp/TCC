def uppCons(texto):
    '''Dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas;
    string -> string'''

    i = 0
    novo_texto = []
    vogais = 'aeiou'

    while i < len(texto):
        if texto[i] not in vogais:
            novo_texto.append(str.upper(texto[i]))
        else:
            novo_texto.append(texto[i])
        i += 1

    return str.join('', novo_texto)