def posLetra(frase,letra,ocorrencia):
    ''' retorna a posição de uma letra em uma string, dito para que ocorrência
    da letra deseja-se saber a posição;
    str,str,int -> int'''
    i=0
    num_ocorrencias=0
    letras=list(frase)
    while num_ocorrencias!=ocorrencia:
        if letras[i]==letra:
            num_ocorrencias=num_ocorrencias + 1
        if i==len(letras)-1:
            return -1
        i=i+1
    return i-1