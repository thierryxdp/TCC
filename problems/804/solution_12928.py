def par(x):
    if x%2==0:
        return x

def filtra_pares(a,b,c,d):
    """ Função que retorna somente os números pares
    int, int, int -> int """
    return (par(a),par(b),par(c),par(d))