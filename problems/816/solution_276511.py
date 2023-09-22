def maiores(lista,n):
    maiores=()
    if lista[0]>n:
        maiores+=(lista[0],)
    if lista[1]>n:
        maiores+=(lista[1],)
    if lista[2]>n:
        maiores+=(lista[2],)
        return maiores