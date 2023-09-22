#Start your python function here
def filtra_pares(tupla):
    lista=[]
    if type(tupla)==tuple and len(tupla)==4:
        for i in tupla:
            if type(i)!=int:
                return []
            elif i%2==0:
                return tuple(lista)