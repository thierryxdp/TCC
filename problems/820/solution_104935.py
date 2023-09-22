def posLetra(texto, L, N):
    '''
    Recebe um texto, uma letra L e N é o numero de ocorrência a ser pesquisada
    Retorna um int com o numero de ocorrencias
    '''
    correncias = []
    for Oc in enumerate(texto):
        if Oc[1] == L:
            correncias.append(Oc[0])
    if N >= len(correncias):
        return -1                    
  	return correncias[N - 1]