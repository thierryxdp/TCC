def lingua_p(palavra):
    '''Recebe uma palavra e retorna sua tradução para a língua do P em minusculas
    	str -> str'''
    palavra = palavra.lower()
    plvr = ''
    vogais = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û', 'ã', 'õ', 'ä', 'ë', 'ï', 'ö', 'ü')
    for letra in palavra:
        if letra in vogais:
            plvr += letra + 'p' + letra
        else:
            plvr += letra
    return plvr