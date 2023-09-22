def lingua_p(palavra):
    '''função que recebe string e retorna para lingua do p
    onde após cada vogal é inserido 'p' e a propria vogal
    str->str'''
    p='p'
    i=0
    palavra=str.lower(palavra)
    l=list(palavra)
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáéíóú':
            l[i]=palavra[i]+p+palavra[i]
            i+=1
    return str.join('',l)