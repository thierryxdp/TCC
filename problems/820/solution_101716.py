def posLetra(st,let,num):
    '''Função que recebe uma string(st), uma letra(let) e 
    um numero(num) para retornar em que posição da string 
    a ocorrência da letra está.
    str, str, int -> int'''
    a=list.count(st,let)
    b=str.index(st,let)
    r=''
    while len(st)>num:
        if st==let:
            i=i+1                                   
        if let!=b:
            i=-1
    return i