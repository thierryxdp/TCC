def filtra_pares(tupla):
    pares = tuple(filter(lambda x: x%2==0, tupla))
    return pares
#O objetivo dessa função é retornar elementos pares ta minha tuplas
#Atraves da propriedade filter eu extraio os valores pares que desejo
#Minha formula para pegar os pares é x%2==0 e ela fica armazenada 
#Juntando todos os elementos eu retorno meus valores pares