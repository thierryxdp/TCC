def conta_numero(numero,matriz):
    
    """
    int,list--->int
    se coloca uma variavel de 0 para que possa ser feita a soma de um
    em um. A cada leitura, se pega a linha de uma matriz e se compara
    cada posicao da matriz com o numero dado na entrada, onde caso sejam
    iguais,soma-se 1 à variavel zerada e se retorna esse valor
    """
    
    ocorrencias=0
    
    for linha in matriz:
        for posicao in linha:
            if posicao==numero:
                ocorrencias+=1
            
    return ocorrencias