def bolos(A,B,C):
    farinha=A
    ovos=B
    colheres=C
    ingredientes=[farinha//2,ovos//3,colheres//5]
    if A>=2 and B>=3 and C>=5:
        list.sort(ingredientes)
        nobolos=ingredientes[0]
        return nobolos
    else:
    	return 0