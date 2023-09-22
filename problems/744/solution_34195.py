def hashtag(s):
    '''função que recebe uma string e insere # no início, 
    no meio e no final dela
    str -> str'''
    if len(s)%2==0 :
        pausar = len(s)//2
    else:
        pausar=(len(s)-1)//2
    return  '#' + s[:pausar] + '#' + s[pausar:] + '#'