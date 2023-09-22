def eh_quadrada(matriz): 
    """Função que identifica se uma matriz é quadrada.
    Observação: uma matriz vazia (sem nenhuma linha nem 
    coluna) é considerada quadrada;
    list -> bool """ 
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if len(matriz) == len(matriz[linha]) and len(matriz[coluna]):
                return True
           
            else: return False
            
    return true