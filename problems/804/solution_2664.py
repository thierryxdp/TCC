#Start your python function here
#Start your python function here
def filtra_pares(tupla):
    """ Funcao recbe uma tupla com quatro elementos inteiros e retorna uma
    nova tupla com apenas os elemtnos pares da tupla original, na mesma
    ordem em que se encontravam """
    
    n1 = tupla[0]
    n2 = tupla[1]
    n3 = tupla[2]
    n4 = tupla[3]
    
    n_tupla = ()
    
    if n1%2 == 0:
        return n_tupla + (n1,)