#Função que dada uma lista de números como entrada, retorna o número de vezes que um elemento da lista é igual ao elemento anterior; lista -> int
def repetidos(lista):
    contador = 0
    posicao = 0
    
    while posicao < len(lista):
          if lista[posicao] == lista[posicao+1]:
              contador = contador + 1
          posicao = posicao + 1
    return contador