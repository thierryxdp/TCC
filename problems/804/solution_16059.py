def par(numero):
        """função booleana que retorna True quando passamos um numero par.
Parametro de entrada:
int
valor de retorno: bool"""
        return numero%2==0

def filtra_pares(t):
    ''' verifica cada elemento da tupla t é par e retorna a uma nova tupla'''
    tup=()     
    if par(t[0]):
        tup=tup+(t[0],)
    if par(t[1]):
        tup=tup+(t[1],)
    if par(t[2]):
        tup=tup+(t[2],)
    if par(t[3]):
        tup=tup+(t[3],)
    return tup