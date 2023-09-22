#Start your python function here
def filtra_pares(tupla):
    tupla2 = ()
    tupla3 = ()
    tupla4 = ()
    tupla5 = ()
    if(tupla[0]%2==0):
        tupla2 = (tupla[0])
        
    elif(tupla[1]%2==0):
        tupla3 = (tupla[1])
        
    elif(tupla[2]%2==0):
        tupla4 = (tupla[2])
        
    elif(tupla[3]%2==0):
        tupla5 = (tupla[3])
        
    return tupla2[0]+tupla3[0]+tupla4[0]+tupla5[0]