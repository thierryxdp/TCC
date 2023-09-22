def lingua_p(palavra):
    '''funcao que recebe como entrada uma palavra em portugues e retorna essa mesma palavra traduzida para a lingua do P
str -> str'''
    palavra=str.lower(palavra)
    palavra_p=palavra
    vogais='aeiou'
    for i in palavra:
        if i in vogais:
            palavra_p=str.replace(palavra_p,i,i+'p'+i)
    return palavra_p