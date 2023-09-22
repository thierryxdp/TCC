#Start your python function here
def filtra_pares(tupla):
    lista=[]
    if type(tupla)==tuple and len(tupla)==4:
        for i in tupla:
            if type(i)!=int:
                return []
                break
            elif i%2==0:
                lista.append(i)
                return tuple(lista)