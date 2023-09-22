def posLetra(string,letra,n):
    '''funcao que recebe como entrada uma string,letra e um
    numero n que indica a ocorrencia desejada da letra e retorna
    a posicao da string onde aquela ocorrencia da letra esta
    str, str, int -> int'''
    proximo1=0
    proximo2=0
    while proximo1<len(string) and proximo2<len(string[:proximo1]):
        if str.count(string,letra)==1:
            return str.find(string)
    proximo1= proximo1+1
    proximo2=proximo2+1