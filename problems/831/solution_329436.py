def lingua_p(palavra):
    """ A funçao lingua_p recebe como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida para a língua do P. 
    Uma palavra foi traduzida para a língua do P quando, após cada vogal da palavra original, é inserida a sequência de letras 'p' mais a vogal original
     str --> str"""
    
    str.lower(palavra)
    resultado = ""
    for x in palavra:
        if x in "aeiouáéíóú":
            resultado = resultado + x + "p" + x
        else: 
            resultado = resultado + x
    return resultado