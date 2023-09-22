def inverte(frase):
    '''Recebe uma frase e retorna outra frase
    com as mesmas palavras da frase na ordem inversa
    sem letras maisculas, e sem pontuação
    string -> string'''
    low = frase.lower()
    separa = low.split()
    
    if '.' in separa:
        sem = separa.replace('.',' ')
        return sem