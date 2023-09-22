def posLetra(frase,letra,num):
    '''uma função posLetra que recebe como entrada uma string, 
    uma letra, e um numero que indica a ocorrencia desejada 
    da letra (1 para primeira ocorrencia, 2 para segunda, etc).
    Sua função deve retornarem que posição da string aquela 
    ocorrencia da letra esta. Caso exista menos ocorrencias 
    da letra do que a ocorrencia pedida, a funcao deve 
    retornar -1. str,str,int - > int '''
    x = 0
    tem = 0
    while x < len(frase) and tem != num:
        if frase[x] == letra:
            tem = tem + 1
            x = x + 1
        else:
            x = x + 1
    if tem >= num:
        return x-1
    else:
        return -1