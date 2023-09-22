def inverte(frase):
    travessao = str.replace(frase,'-',' ')
    virgula = str.replace(travessao,',',' ')
    dois_pts = str.replace(virgula,':',' ')
    ponto_virg = str.replace(dois_pts,';',' ')
    ponto = str.replace(ponto_virg,'.',' ')
    exclamacao = str.replace(ponto,'!',' ')
    interrogacao = str.replace(exclamacao,'?',' ')
    
    sem_pont = interrogacao
    
    minusculo = str.lower(sem_pont)
    
    split = str.split(minusculo)
    
    return str.join(split,)