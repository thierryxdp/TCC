def filtraMultiplos(L,N):
    "Recebe uma lista L e um numero N, ambos do tipo inteiro e retorna os elementos da lista que são multiplos de N"
    "entrada lista : int"
    "saida lista:int"
    lista=L
    Lista2=[]
    x=0
    Nu=len(lista)
    while(x<Nu):
        if lista[x]%N==0:
            Lista2=Lista2+[lista[x]]
        x=x+1
    return Lista2