def filtraMultiplos(x,y):
    ''' Função que retorna todos os elementos contidos 
  em 'lis' list,int -> list'''
    z = []
    w = 0
    while w < len(x):
        if x[w] % y == 0:
            z += (x[w] ,)
            w += 1
            return z