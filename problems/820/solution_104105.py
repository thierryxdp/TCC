def posLetra(string, letra,n):
    '''essa funçao recebe uma string, uma letra e um numero e retorna posição da string que a ocorrencia
n da letra está
str,str, int -> '''
    i=0
    a=0
    if str.count(string,letra) < n:
        return -1
    else:
        while i< len(string):
            if letra==string[i]:
                a=a+1
            if a==n:
                return i
            i=i+1