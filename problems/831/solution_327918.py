def lingua_p(palavra):
    '''funcao que retorna a palavra traduzida para a lingua do p, onde
    apos cada vogal, se insere um p seguido da propria vogal;
    string->string'''
    str.lower(palavra)
    resultado = ""
    for x in palavra:
        if x in "aeiouáéíóú":
            resultado = resultado + x + "p" + x
        else: 
            resultado = resultado + x
    return resultado