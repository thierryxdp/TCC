def filtra_pares(tupla):
    """
    	Função que recebe quatro números e retorna apenas os pares 
        na ordem em que se encontravam.
        int,int,int,int->tupla
    """
     if tupla[0]%2==0 and tupla[1]%2==0 and tupla[2]%2==0 and tupla[3]%2==0:
        return (tupla[0],tupla[1],tupla[2],tupla[3])