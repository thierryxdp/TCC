def lingua_p(palavra):
    '''Função que recebe uma palavra e a retorna na língua do p,
    	ou seja, após cada vogal da palavra original, é inserida uma 
        sequência de lestras 'p' mais a vogal da palavra original, 
        ignorando a diferença entre letra maiúscula e minúscula e
        retornando tudo em letra minúscula
        
        str -> str'''
    c=[]
    for i in range(len(palavra)):
        if str.lower(palavra[i]) in 'aáàâãeéêiíoóôõuú':
            c = c + [str.lower(palavra[i])] + ['p'] + [str.lower(palavra[i])]
        else:
            c = c + [str.lower(palavra[i])]
    return str.join('',c)