def lingua_p(string):
    '''Função que recebe uma palavra e traduz para outra língua
    chamada lingua p.
    entrada da função: str
    saída da função: str'''
    
    palavra = ""
    vogais = "aeiouáéíóúãõ"
    for i in string:
        if i in vogais:
            palavra = palavra + (i + "p" + i)
        else:
            palavra += i
    return str.lower(palavra)