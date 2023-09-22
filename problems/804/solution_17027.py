def filtra_pares(num):
    '''Esta função recebe uma tupla com números inteiros, verifica qual
elemento é par e põe este ineiro em uma tupla na mesma ordem da tupla inicial,
retornando uma tupla com os elementos pares na ordem em que vieram inicialmente..
tuple --> tuple'''
    num2 = ()
    if num[0]%2 == 0:
        num2 += (num[0],)
        
    if num[1]%2 == 0:
        num2 += (num[1],)
        
    if num[2]%2 == 0:
        num2 += (num[2],)
        
    if num[3]%2 == 0:
        num2 += (num[3],)
        
    return num2