def qtd_divisores(num):
    
    """
    int--->int
    Cria-se uma variavel com o 0. Nessa variavel, soma-se 1 a cada vez
    que o numero da entrada é divisível. Para isso, é utilizado o comando
    range com o comando i, para que a leitura seja feita do 1 até o numero
    em si(foi colocado num+1 pois apenas num faria com que o resultado
    tivesse 1 divisor a menos,sem considerar a divisao do numero por ele mesmo)
    """
    soma=0
 
    for i in range(1,num+1):
        if num%i==0:
            soma+=1
            
    return soma