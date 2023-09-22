def faltante(pecas):
    '''Diz qual a peça que falta em um quebra-cabeça;
    list -> int'''
    falta = 1 #Números a serem testados
    contador = 0 
    pecas.sort()#Deixa a lista em ordem crescente
    comparador = list(range(pecas[0],pecas[-1]))#Uma lista de onde sairão os números que faltam
    while contador < len(pecas):
          if pecas.count(falta) == 0:#Indica qual o número que falta
             return comparador[contador]

          else:
              falta = falta + 1
              contador = contador + 1