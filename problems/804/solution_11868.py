def filtra_pares(tupla):
    '''funcao que filtra numeros pares dada
    uma tupla como parametro
    entrada: tuple
    saida: tuple
    '''
    tupla1= (tupla[0]%2==0)
    tupla2= (tupla[1]%2==0)
    tupla3= (tupla[2]%2==0)
    tupla4= (tupla[3]%2==0)
    return (str(tupla1),str(tupla2),str(tupla3),str(tupla4))