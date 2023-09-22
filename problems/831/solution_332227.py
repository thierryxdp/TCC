def lingua_p(palavra):
    '''
    função que recebe como parâmetro uma palavra e retorna esta mesma palavra traduzida para a língua do P;
    str -> str
    '''
	palavra = str.lower(palavra)
    for letra in palavra:
        if 'aeiou' in palavra:
            palavra = str.replace(palavra,letra,letra+'p'+letra)
    return palavra