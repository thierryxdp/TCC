def posLetra(s,l,n):
    '''Função que tem como entrada uma string(s), uma letra(l) e um 
    numero(n) que indica a ocorrência desejada de l na string. Ela retorna
    a posição de s que a nª letra(l) aparece, se não for possível retorna -1
    str, str, int -> int'''
    i=0
    pos=0
    if n > str.count(s,l):
            return -1
    while i<len(s):
        if s[i]==l:
            pos= i
            if pos==n:
                return str.index(s[i],l)
        i=i+1
    return pos