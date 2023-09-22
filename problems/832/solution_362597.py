def eh_quadrada(matrix):
    """Função que dada uma matrix, retorna se essa matrix é quadrada ou não. Entrada -> Matrix; Saida -> bool"""
    if matrix == []:
        return True
    else:
        coluna = len(matrix[0])
        linha = len(matrix)
         return coluna == linha