def posLetra(s,letra,n):
    '''Retorna a posição da ocorrência 'n' da letra de entrada
       na string 's';
       str, str, int -> int'''
    qtdLetra=s.count(letra)

    if n>qtdLetra:
        return -1

    count=0
    while count<n:
        pos=s.index(letra)
        s=s[:pos]+s[pos+1:]
        count+=1
    return pos+n