#Start your python function here
def filtra_pares(elem1, elem2, elem3, elem4):
    
    elementos = (elem1, elem2, elem3, elem4);
    elemPares = elementos[::2]
    
    return elemPares