def filtra_pares(t):
    '''funcao que recebe uma tupla com quatro 
    interios e retorna os pares dessa tupla'''
    tupla1= t[0]%2
    tupla2= t[1]%2
    tupla3= t[2]%2
    tupla= t[3]%2
    return [tupla1==0,tupla2==0,tupla3==0,tupla4==0]