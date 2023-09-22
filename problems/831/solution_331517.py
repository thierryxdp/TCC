def lingua_p(palavra):
    '''função que recebe uma palavra e retorna essa mesma palavra 
    em letras minúsculas e traduzida para a língua do P, ou seja,
    após cada vogal da palavra original será introduzida uma letra P e
    mais uma vogal na palavra traduzida.
    entrada:string
    saída:string'''
    p=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáéíóú':
            p = p + palavra[i]+ 'p' + palavra[i]
        else:
            p=p+palavra[i]
    return p