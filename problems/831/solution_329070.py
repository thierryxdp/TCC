def lingua_p(palavra):
    ''' funcao que recebe como parametro uma palavra(em portugues)
     e retorne esta mesma palavra traduzida para a lingua
     do P, a funcao nao distingue letras maiuscula e minuscula
     retornando sempre a palavra traduzida em letras minusculas
     string->string'''
    for elementos in palavra:
        if elementos in 'aeiou':
            frase_tratada= elementos+ 'p'+ elementos
        if elementos not in 'aeiou':
            frase_tratada= elementos
    return frase_tratada