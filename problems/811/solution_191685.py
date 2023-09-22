def colchao(medidas,H,L):
    '''Determina se há possibilidade de um colchão de medidas determinadas por
     A,B e C passar por uma porta de altura H e largura L;
     entrada: lista, int, int;
     saída: lista, int, int;
     '''
    if (medidas[2]<=H):
      medidas = medidas[ :-1]
    elif(medidas[1]<=H):
      medidas = medidas[ : :2]
    elif(medidas[0]<=H):
      medidas = medidas[1:]
    if (medidas[1]<=L):
      return True
    elif (medidas[0]<=L):
      return True
    else:
      return False