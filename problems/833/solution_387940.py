def conta_numero(numero,matriz):
	""" Esta Função retorna a quantidade de vezes que um número X aparece na matriz 
	int,dict -> int """

matriz2=[]
linha1 = []
linha2 = []
qntde=0
linha1.append(0)
for l in range(numerodelinhas):
    for c in range(numerodecolunas):
        qntde = 0
        if(linha1.count(matriz[l][c])==0):
            if(l==0 and c == 0):
                linha1[0]=matriz[0][0]
            if(l != 0 or c != 0):
                linha1.append(matriz[l][c])
            for n in range(numerodelinhas):
                qntde = qntde + matriz[n].count(matriz[l][c])
            linha2.append(qntde)

matriz2.append(linha1)
matriz2.append(linha2)
cm2=0
for n in matriz2[0]:
    print (matriz2[0][cm2]," - ",matriz2[1][cm2])
    cm2+=1