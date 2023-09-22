def uppCons(palavra):
    lista = list(palavra)
    lista2 = [b,c,d,f,g,h,j,k,l,m,z,p,q,r,s,t,v,w,x,y,z]
    lista3 = list(lista2)
    i = 0 
    while i < len (lista):
        j=0
        while j < len (lista3):
            if lista[i] == lista3[j]:
                lista[i].upper()
            j+=1
        i+=1
    return (lista)