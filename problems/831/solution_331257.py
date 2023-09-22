def lingua_p(palavra):
    '''Recebe una palavra e retorna a mesma
    traduzida na língua do P, ou seja, após 
    cada vogal da palavra original, é inserida
    a sequência de letras 'p' mais a vogal original'''
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra in "aeiou":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP