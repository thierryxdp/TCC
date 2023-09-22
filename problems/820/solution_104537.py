def posLetra(string,letra,ocorrencia):
    '''Dada uma string, uma letra e um inteiro que represente a
    ocorrencia dessa letra na string, a função retorna em que posição
    da string se encontra a ocorrencia da letra. A função retorna -1
    caso existam menos ocorrencias da letra do que a occorencia de
    entrada. str,str,int -> int'''
   
    x=list(string)
    proximo=1

    if ocorrencia > list.count(x,letra):
        return -1
    else:
        while proximo<ocorrencia:
           
            x[list.index(x,letra)]='Ç'
            proximo=proximo+1
    return list.index(x,letra)