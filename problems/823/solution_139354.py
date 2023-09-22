def faltante(L):
    '''Função que dada uma lista com tamannho N - 1 contendo números inteiros
    e não repetidos de 1 a N, e retorna um número inteiro x que pertence
    ao intervalo [1,N] mas que não pertence a lista de entrada L;
    list -> int'''

    ordem = list.sort(L) 
    posicao = 0
    
    while posicao<len(L):
          if L[posicao] == posicao+1:            
            posicao = posicao + 1          
          else:
              break
    return posicao+1