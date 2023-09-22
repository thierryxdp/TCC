def eh_quadrada(matriz):
    '''Uma função que dada uma matriz retornar um boleano
    se é ou não um quadrado'''
    if matriz == []:
          return True
    elif len(matriz) == len(matriz[0]):
          return True
    else:
          return False