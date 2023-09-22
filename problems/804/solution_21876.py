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
        newTruple[0] = truple[0]
    if resto1 == 0:
        newTruple[1] = truple[1]
    if resto2 == 0:
        newTruple[2] = truple[2]
    if resto3 == 0:
        newTruple[3] = truple[3]
    
	return newTruple