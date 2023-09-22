def lingua_p(palavra):
    '''uma função que receba como parâmetro uma palavra (em pt) e retorne esta mesma palavra
traduzida para a língua do P. Uma palavra foi traduzida para a língua do P quando, após cada vogal
da palavra original,  ́e inserida a sequência de letras p mais a vogal original.'''
    # str > str
    vogal = '''aeiouãéíóúãõôâêîûAEIOUÁÉÍÓÚÃÕÂÊÎÔÛ'''
    for i in palavra:
        if i in vogal:
            palavra = palavra.replace(i, i+'p'+i,1)
    return palavra