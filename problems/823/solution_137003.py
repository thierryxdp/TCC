def faltante(l):
    "recebe uma lista de numeros e retorna o numero que falta no intervalo [1,N]" 
    "sendo N o maior numero da lista"
    "entrada: int. saida: int."
    list.sort(l)
    if 1 not in l:
        return 1
    if l[-1]<len(l)+1:
        return len(l)+1
    x=0
    numerofora=0
    while x<len(l)-1:
        if l[x+1]-l[x]>1:
            numerofora=numerofora+l[x]+1
        x=x+1
    return numerofora