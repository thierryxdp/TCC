def posLetra(string,letra,n):
    '''funcao que recebe como entrada uma string,letra e um
    numero n que indica a ocorrencia desejada da letra e retorna
    a posicao da string onde aquela ocorrencia da letra esta
    str, str, int -> int'''
    proximo1=0
    proximo2=0
    while proximo1<len(string) and proximo2<len(string[:proximo]):
        if string[proximo1]!= string[:proximo1][proximo3]:
            return str.index(string)+1
    proximo1= proximo1+1
    proximo2=proximo2+1