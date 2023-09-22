def linguap (palavra) :
    """Funcao que recebe como parametro uma palavra e retorna esta mesma palavra traduzida para a lingua do P"""
    palavra = str.lower(palavra)
    palavra_final = ''
    vogais = 'aáàãâeéêiíoóôõuú'
    for i in palavra :
        palavra_final = palavra_final+i
        if i in vogais:
            palavra_final = palavra_final + 'p' + i
    return palavra_final