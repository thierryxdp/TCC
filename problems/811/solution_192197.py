def colchao(medidas, H, L):
  '''verifica se esse colchao passa pela altura q é H e largura L da porta
  :param medidas: list->list
  :param H: int->int
  :param L: int->int
  :return: bool->bool
  '''
 [A,B,C] = medidas
    
    if A and B > H and L:
    return False

    else:
        return True