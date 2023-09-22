def filtra_pares(tupla):
   '''Função que recebe uma tupla com quatro elementos
   inteiros como parâmetro, e retorna uma nova tupla contendo apenas
   os elementos pares da tupla original'''
    t=()
    if tupla[0]%2==0:
        t+=(tupla[0],)
        
    if tupla[1]%2==0:
        t+=(tupla[1],)
    
    if tupla[2]%2==0:
        t+=(tupla[2],)
        
    if tupla[3]%2==0:
        t+=(tupla[3],)
     
    return t()