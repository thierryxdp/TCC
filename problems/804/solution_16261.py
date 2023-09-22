def filtra_pares(f):
    '''função que recebe uma tupla t
    com 4 elementos inteiros como parâmetro
    e retorna uma nova tupla contendo apenas
    os elementos pares
    '''
  
    e1=f[0]%2               
    e2=f[1]%2
    e3=f[2]%2
    e4=f[3]%2
    
    if e1 == 0 and e2 == 0 and e3 == 0 and e4 == 0:
        return (f[0],f[1],f[2],f[3])