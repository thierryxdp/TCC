def posLetra(s,l,n):
    '''Função que tem como entrada uma string(s), uma letra(l) e um 
    numero(n) que indica a ocorrência desejada de l na string. Ela retorna
    a posição de s que a nª letra(l) aparece, se não for possível retorna -1
    str, str, int -> int'''
    i=0
    while i < len(s):
        if n > str.count(s,l):
            return -1
        else:
            str.index(s,l,i)
        i=i+1
    return str.index(s,l,i)