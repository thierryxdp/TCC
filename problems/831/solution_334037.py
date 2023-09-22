def lingua_p(string):
    '''função que recebe uma palavra e traduz para a língua do p
    entrada da função: str
    saída da função: str '''
    palavra = ""
    vogais = "aeiouáéíóúâêôãõ"
    for i in string:
        if i in vogais:
            palavra = palavra + (i + "p" + i)
        else:
            palavra += i
    return str.lower(palavra)