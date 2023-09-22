def lingua_p(palavra):
    '''funcao que recebe como entrada uma palavra em portugues e retorna essa palavra traduzida para a lingua do P
    str -> str'''
    palavra=str.lower(palavra)
    vogais='aeiou'
    palavra_p=''
    for vogais in palavra:
        palavra_p=palavra_p+str.replace(palavra,vogais,vogais+'p')
    return palavra_p