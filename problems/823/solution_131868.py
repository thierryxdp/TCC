def faltante(lista):
    
    novalista = list.sort(lista)
    i= novalista[0]
    f= novalista[-1] + 1
    original = list(range(i,f))
    
    while original != lista: