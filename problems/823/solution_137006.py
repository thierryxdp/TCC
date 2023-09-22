def faltante(lista):
    l=lista[:]
    l.sort()
    cont=0
    perdido=-1
    while cont <len(1):
        if l[cont]==cont+1:
            cont+=1
        else:
            perdido= cont+1
            cont= len(1)
    if perdido== -1:
        perdido = len(1)+1
        return perdido