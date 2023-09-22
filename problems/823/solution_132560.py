def faltante(pecas):
    '''Diz qual a peça que falta em um quebra-cabeça;
    list -> int'''
    falta = 1 #Números a serem testados 
    contador = 0 
    pecas.sort()#Deixa a lista em ordem crescente
    comparador = list(range(1 - pecas[0],pecas[-1]+2))#Uma lista que será comparada com a original
    while contador < len(comparador):
         
          if falta in comparador and falta not in pecas:
              return falta

          else:
              falta = falta + 1
              contador = contador + 1