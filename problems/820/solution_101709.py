def posLetra(st,let,num):
    '''Função que recebe uma string(st), uma letra(let) e 
    um numero(num) para retornar em que posição da string 
    a ocorrência da letra está.
    str, str, int -> int'''
    a=list.count(st,let)
    b=st.index(let)
    resultado=r
    while len(st)>num:
        if let==b:
            r=b                                   
        if let!=b:
            r=-1
    return r