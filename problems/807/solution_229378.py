def conta_frases(x):
    '''
    
    '''
    pontuacao = ['!','?',',','...']
    texto = x.split()
    cont = 0 
    for lac_pal in texto:
        for lac_pontuacao in pontucao:
            if lac_pontuacao in lac_pal:
                cont+=1
                return cont