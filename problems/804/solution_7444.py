def filtra_pares(tuple):
    '''funcao que filtra os elementos pares e os retorna
    Parametros:
    1,2,3,4: int
    Saida:
	int'''
   	par = () 
    if tuple[0]%2==0:
        par= par+tuple[0]
    if tuple[1]%2==0:
        par= par+tuple[1]
    if tuple[2]%2==0:
        par= par+tuple[2]
    if tuple[3]%2==0:
        par= par+tuple[3]
    if tuple[4]%2==0:
        par= par+tuple[4]
    return par