def lingua_p(string):
    '''Função que recebe uma palavra e retorna esta mesma
    palavra traduzida para a língua do P.
    str -> str'''
    
    palavra = ""
    vogais = "aeiouáéíóúãõ"
    for i in string:
        if i in vogais:
            palavra = palavra + (i + "p" + i)
        else:
            palavra += i
    return str.lower(palavra)