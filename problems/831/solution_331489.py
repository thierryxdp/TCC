# Questão 6 - MT
def lingua_p(palavra):
    '''Traduz uma palavra em português para uma na língua do P
    exemplo --> epexepemplopo
    str --> str'''

    # variável para guardar a palavra traduzida
    palavra_p = ''

    # itera pela palavra
    for i in palavra.lower():
        # verifica se o caractere em i é uma vogal
        if i in 'aáàâãeéèêiíìîoóôõuúùû':
            # adiciona p entre a vogal em i à palavra traduzida
            palavra_p += i + 'p' + i
        else:
            # adiciona a consoante em i à palavra traduzida
            palavra_p += i
    return palavra_p