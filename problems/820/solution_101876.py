def posLetra(string,letra,ocorrencia):
    '''Função que recebe como entrada uma string, uma letra e um numero
    que indica a ocorr~encia desejada da letra e retorn em que posição
    da string aquela ocorrência da letra está. Caso exista menos ocorrências
    da letra do que a ocorrência pedida, a função retorn -1; str,str,int->int'''
    i=0
    posicao=-1
    while i<len(string):
        if string[i]==letra and str.count(string,letra,0,i+1)==ocorrencia:
            posicao= i
        i+=1
    return posicao