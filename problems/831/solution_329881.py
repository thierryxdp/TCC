def lingua_p(palavra):
    '''funcao que recebe como entrada uma palavra em portugues e retorna essa mesma palavra traduzida para a lingua do P
str -> str'''
    palavra=str.lower(palavra)
    palavra_p=''
    vogais='aeiouáéíóúãõê'
    for i in palavra:
        if i in vogais:
            palavra_p += i + 'p' + i
        else:
            palavra_p += i
    return palavra_p