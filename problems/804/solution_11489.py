def filtra_pares(tupla):
    '''Função que recebe uma tupla com quatro
       números inteiros e retorna uma nova 
       tupla apenas com os números pares da 
       original
       tuple -> tuple'''
    
   if tupla[0]%2 == 0:
    tupla = tupla[0]
   if tupla[1]%2 == 0:
    tupla = tupla[1]
   if tupla[2]%2 == 0:
    tupla = tupla[2]
   if tupla[3]%2 == 0:
    tupla = tupla[3]
    
    return tupla