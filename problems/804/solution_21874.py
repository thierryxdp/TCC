def filtra_pares(truple):
#Recebe uma trupla e retorna uma nova tupla contendo
#apenas os elementos ímpares da trupla-parâmetro
# trupla --> trupla
    resto0 = truple[0]%2
    resto1 = truple[1]%2
    resto2 = truple[2]%2
    resto3 = truple[3]%2
    newTruple = ()
    
	if resto0 == 0:
        newTruple.append(truple[0])
    if resto1 == 0:
        newTruple.append(truple[1])
    if resto2 == 0:
        newTruple.append(truple[2])
    if resto3 == 0:
        newTruple.append(truple[3])
    
	return newTruple