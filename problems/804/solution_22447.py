#Start your python function here
def filtra_pares(w,x,y,z):
   ''' Função que recebe uma tupla com 4 elementos inteiros e 
retorna uma nova tupla apenas com os elementos pares.
int, int, int, int -> tuple'''
    filtragem=()
    if (w,x,y,z [0]%2)==0:
        filtragem+=(w,x,y,z[0],)
    if (w,x,y,z [1]%2)==0:
        filtragem+=(w,x,y,z[1],)
    if (w,x,y,z [2]%2)==0:
        filtragem+=(w,x,y,z[2],)
    if (w,x,y,z [3]%2)==0:
        filtragem+=(w,x,y,z[3],)
    return filtragem