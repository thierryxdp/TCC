def busca(palavra,matriz):
    '''Dada uma matriz a função faz uma 
       busca por setor da empresa e 
       retorna os dados dos funcionarios
       daquele setor''' 
    i=0
    resultado = []
    while i < len(matriz):
        matriz2 = matriz[i]
        if matriz2[2] == palavra:
            kaka = [matriz2[0] , matriz2[1] , matriz2[3]]
            resultado = [kaka] + resultado
            list.reverse(resultado)
        i = i +1
        
    return resultado