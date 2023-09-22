def lingua_p(palavra):
    ''' funcao que recebe como parametro uma palavra(em portugues)
     e retorne esta mesma palavra traduzida para a lingua
     do P, a funcao nao distingue letras maiuscula e minuscula
     retornando sempre a palavra traduzida em letras minusculas
     string->string'''
    indice = 0
    for indice in palavra:
        if indice in 'aeiou':
            frase_tratada= palavra[indice]+ 'p'+ palavra[indice]
        if palavra[indice] not in 'aeiou':
            frase_tratada=palavra[indice]
        indice = indice + 1
    return frase_tratada