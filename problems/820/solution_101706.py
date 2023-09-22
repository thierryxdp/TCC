def posLetra(st,let,num):
    '''Função que recebe uma string(st), uma letra(let) e 
    um numero(num) para retornar em que posição da string 
    a ocorrência da letra está.
    str, str, int -> int'''
    a=list.count(st,let)
    i=''
    while a>num:
        if let==st[num]:
            i=i
        if let!=st[num]:
            i=-1
    return i