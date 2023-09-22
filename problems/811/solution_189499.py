def colchao(dimensoes,H,L):
    """Essa função informa se um colchão passa pelas portas dadas as dimensões do
colchão, a altura e a largura das portas em centímetros, retornando True se o colchão
passa pelas portas e False em caso contrário.
Os parâmetros de entrada são uma lista(dimensoes) com as dimensões A, B e C do colchão em
centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes
respectivamente à altura e à largura das portas em centímetros. 
list,int,int -> bool"""
    return (dimensoes[0]<=H and dimensoes[1]<=L) or (dimensoes[0]<=L and dimensoes[1]<=H)