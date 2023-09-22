def eh_quadrada(lista):
      '''identifica se uma matriz dada como argumento é quadrada, 
retornando True caso seja
e False caso nao seja'''
    
    if lista == []:
        return True
    elif len(lista) == len(lista[0]):
        return True
   
    else:
        return False