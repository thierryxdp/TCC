def maiores(*num):
    cont=maior=0
    for valor in num:
        if cont==0:
            maior=valor
		else:
            if valor>maior:
                maior=valor
        cont+=1