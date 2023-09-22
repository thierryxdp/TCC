import re 
def lingua_p(palavra):
    '''uma função que receba como parâmetro uma palavra (em pt) e retorne esta mesma palavra
traduzida para a língua do P. Uma palavra foi traduzida para a língua do P quando, após cada vogal
da palavra original,  ́e inserida a sequência de letras p mais a vogal original.'''
    # str > str
    vogal = '''aeiouãéíóúãõôâêîûAEIOUÁÉÍÓÚÃÕÂÊÎÔÛ'''
    u = list(palavra)
    for n, i in enumerate(u):
        if i in vogal:
            u[n] = i+'p'+i
        palavra = ''.join(u)
    return palavra