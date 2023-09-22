def posLetra(st,let,num):
    '''Função que recebe uma string(st), uma letra(let) e 
    um numero(num) para retornar em que posição da string 
    a ocorrência da letra está.
    str, str, int -> int'''
    a=list.count(st,let)
    b=str.index(st,let)
    i=0
    while a>num:
        if st[::1]==let:
            i=i+1
        if st[::1]!=let:
            i=-1
    return i