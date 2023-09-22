def soma_h(numero):
    
    """ Esta função exprime uma soma. Usaremos estruturas de repetições for
        para isso.
        Esta série em específica recebe o nome de Série Harmônica. Séries são
        caracterizadas por ter infinitos termos. Entretanto, é possível usar valores
        que não tendem ao infinito. Estes são os valores que usamos na função.
        Obs.: Sempre teremos um erro por não usar valores que não tendem ao infinito.
        int -> float
    """

    soma_harmonica = 0

    for n in range(1,numero+1):
        
        soma_harmonica = soma_harmonica + (1/n)
        
    return round(soma_harmonica,2)