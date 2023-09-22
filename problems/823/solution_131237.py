def faltante(L):
    '''funcao que dada uma lista de tamanho N-1 contendo numeros inteiros nao repetidos, retorna o numero inteiro x
       pertencente ao intervalo, que nao se encontra na lista de entrada
       list -> int '''
    i = 1
    numfalta = 0
    list.sort(L)
    if(len(L) == 1):
        return 1
    if(L[0] != 1):
    	return 1
    while(i < len(L)):
        if((L[i]-1) == L[i-1]):
            i += 1
        else:
            numfalta = L[i]-1
            i += 1
    if(numfalta == 0):
        numfalta = len(L) + 1
    return numfalta