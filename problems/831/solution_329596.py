def lingua_p(palavra):
    '''funcao que recebe como entrada uma palavra em portugues e retorna essa palavra traduzida para a lingua do P
    str -> str'''
    palavra=str.lower(palavra)
    vogais='aeiou'
    for vogais in palavra: