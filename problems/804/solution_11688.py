def filtra_pares(t):
    '''funcao que recebe uma tupla com quatro 
    interios e retorna os pares dessa tupla'''
    tupla1= (t[0]%2==0)
    tupla2= (t[1]%2==0)
    tupla3= (t[2]%2==0)
    tupla4= (t[3]%2==0)
    return [int(tupla1),int(tupla2),int(tupla3),int(tupla4)]