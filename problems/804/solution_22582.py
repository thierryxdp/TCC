#Start your python function here
def epar(num):
    
    return num%2==0

def filtra_pares(lista):
    
    resultado = ()
    
    if epar(lista[0]):
        resultado += lista[0:1]
    if epar(lista[1]):
        resultado += lista[1:2]
    if epar(lista[2]):
        resultado += lista[2:3]
    if epar(lista[3]):
        resultado += lista[3:]    
    return resultado