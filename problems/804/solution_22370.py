#Start your python function here
def filtra_pares(w,x,y,z):
    ''' Função que recebe uma tupla com 4 elementos inteiros e 
    retorna uma nova tupla apenas com os elementos pares.
    int, int, int, int -> tuple'''
    nova =[]
    filtragem = nova+w,x,y,z
    if (w%2==0 and x%2 ==0 and y%2 ==0 and z%2 == 0):
        return filtragem