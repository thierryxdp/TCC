def posLetra(frase,letra,ocorrencia):
    ''' retorna a posição de uma letra em uma string, dito para que ocorrência
    da letra deseja-se saber a posição;
    str,str,int -> int'''
    i=0
    num_ocorrencias=0
    while num_ocorrencias!=ocorrencia:
        if list(frase)[i]==letra:
            num_ocorrencias=num_ocorrencias + 1     
        i=i+1
    return i