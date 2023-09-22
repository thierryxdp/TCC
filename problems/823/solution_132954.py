def faltante(L):
    """Funcao que, dada uma lista com N-1 inteiros numerados 
    de 1 a N, descobre qual numero inteiro deste intervalo 
    esta faltando. O parametro de entrada e uma lista L de 
    tamanho N-1 contendo numeros inteiros(nao repetidos) de 
    1 a N. A funcao retorna o numero inteiro que pertence ao 
    intervalo [1,N] mas que nao pertence a lista de entrada 
    L;
    lista->int"""
    
    L1=L[:]
    list.sort(L1)
    
    i=0
    n=0
    
  	if L[0]!=1:
    return 1
	
    while i<len(L1):
        if L1[i]==i+1:
            n=n+1
        i=i+1
    return (n+1)