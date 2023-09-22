def filtra_pares(a,b,c,d):
    """ Função que retorna somente os números pares 
    int,int,int,int -> int """
    if (a or b or c or d)%2==0:
        return (a,b,c,d)