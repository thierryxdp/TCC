def faltante(L):
'''retorna o numero inteiro que pertence ao intervalo 1,N sem pertencer a lista de entrada L.lista->int'''
i=0
while i<len(L):
    if L[i+1]==L[i]+2:
        return L[i]+1
    i=i+1