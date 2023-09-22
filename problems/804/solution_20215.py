#Start your python function here
def filtra_pares(e):
    lista=[]
    if type(e)==tuple and len(e)==4:
        for i in e:
            if type(i)!=int:
                lista=[]
                break
            elif i%2==0:
                lista.append(i)
                return tuple(lista)