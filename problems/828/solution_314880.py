def primo(n):
    lista=[]
    contador=0
    while contador<n:
        if n%(contador+1)==0:
            list.append(lista,contador+1)
        contador=contador+1
    if len(lista)!=2:
        return False
    else:
        return True