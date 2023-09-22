#Start your python function here
 def filtra_pares(x):
    """ Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original
    tuple(int,int,int,int)->tuple(int,int,int)
    """
    novaTup = ()
    if x[0] %2 == 0:
        novaTup += (x[0],)
    if x[1]%2==0:
        novaTup +=(x[1],)
    if x[2]%2==0:
        novaTup += 9x[2],)
    if x[3]%2==0:
        novaTup += (x[3],)
        
        return novaTup