# A função recebe uma string, uma letra e um numero que indica a ocorrência desejada da letra e
# retorna em que posição da string aquela ocorrência da letra está. Caso exista menos ocorrências 
# da letra do que a ocorrência pedida, a função deve retornar -1
# string,string,int->int
#
def posLetra(string,letra,numero):
    i=0
    c=0
    a=str.count(string,letra)
    if a < numero:
        return -1
    while c < numero:
        if string[i] == letra:
            c=c+1
        i=i+1
    return i-1