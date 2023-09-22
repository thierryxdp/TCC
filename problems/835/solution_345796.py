#Questão4
def melhor_volta(matriztempo):
    '''
    A função retorna quem deu a melhor volta
    em qual o tempo.
    list -> (int,int,int
    '''
    menortempo = matriztempo[0][0]
    qualvolta = 1
    qualcorredor = 1
     
    for l in range(len(matriztempo)):
        for c in range(len(matriztempo[l])):
            if matriztempo[l][c] < menortempo:
                menortempo = matriztempo[l][c]
                qualvolta = l + 1
                qualcorredor = c + 1
    return (qualvolta,qualcorredor,menortempo)