#Start your python function here
def filtra_pares(x):
    '''Função que recebe uma tupla com 4 elementos inteiros e 
retorna uma nova tupla apenas com os elementos pares.
int, int, int, int -> tuple'''
    filtragem = ()
    if (x [0]%2)==0:
        filtragem += (x[0],)
    if (x [1]%2)==0:
        filtragem += (x[1],)
    if (x [2]%2)==0:
        filtragem += (x[2],)
    if (x [3]%2)==0:
        filtragem += (x[3],)
        return filtragem