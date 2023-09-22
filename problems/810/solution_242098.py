def inverte(frase):
    '''retorna o inverso da frase fornecida sem ter nenhuma letra maiuscula ou pontuações
    str -> str'''
    travessao = str.replace(frase,'-',' ')
    virgula = str.replace(travessao,',',' ')
    dois_pts = str.replace(virgula,':',' ')
    ponto_virg = str.replace(dois_pts,';',' ')
    ponto = str.replace(ponto_virg,'.',' ')
    exclamacao = str.replace(ponto,'!',' ')
    interrogacao = str.replace(exclamacao,'?',' ')
    
    sem_pontuacao = interrogacao
    
    minusculo = str.lower(sem_pontuacao)
    
    split = str.split(minusculo)
    
    return ' '.join(split[::-1])