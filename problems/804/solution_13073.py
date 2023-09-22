def filtra_pares(x,y,w,z):
    """ Função que retorna somente os números pares 
    int,int,int,int -> int """
    if (x or y or w or z)%2==0:
        return (x,y,w,z)