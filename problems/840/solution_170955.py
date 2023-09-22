def bolos(A,B,C):
	farinha=A
	ovos=B
	colheres=C
    ingredientes=[farinha//2,ovos//3,colheres//5]
#2,3,5
#A>=2,B>=3,C>=5
#sort
#ingredientes[0]
if A>=2 and B>=3 and C>=5:
    list.sort(ingredientes)
    return ingredientes[0]
else:
    return 0