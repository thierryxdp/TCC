#Start your python function here
def filtra_pares(elementos):
    """ Funcao que retorna apenas os elementos pares da tupla recebida como parametro;
    	tuple -> tuple
    """
    elementos_pares = ()
    for elemento in elementos:
        if elemento % 2 == 0:
            elementos_ pares += (elemento)
            
    return elementos_pares