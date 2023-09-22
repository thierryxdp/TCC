def eh_quadrada(matriz):
  def obter_dimensao(m):
    # Verifica se todas as linhas da matriz
    # possuem o mesmo tamnho
    if len({len(i) for i in m}) > 1:
        raise TypeError('Matriz 2D invalida.')

    # Calcula quantidade de linhas na matriz
    linhas = len(m)

    # Se nao houverem linhas na matriz
    # assume zero colunas
    colunas = len(m[0]) if linhas else 0

    return (linhas, colunas)