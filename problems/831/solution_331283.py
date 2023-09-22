def lingua_p(palavra):
    '''Recebe una palavra e retorna a mesma
    traduzida na língua do P, ou seja, após 
    cada vogal da palavra original, é inserida
    a sequência de letras 'p' mais a vogal original
    str -> str'''
    
    lp = ''
    palavra = palavra.split()
    vogal = 'aeiou'
    vogal = vogal.split()
    for i in palavra:
        if i in vogal:
            lp += i + 'p' + i
        else:
            lp += i
    return lp