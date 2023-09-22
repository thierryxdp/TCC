def retira_pontuacao(frase:str) -> str:
    """Substitui todas as pontuações por espaços vazios
    
       Parameters:
       frase: frase a ser modificada
       
       Returns:
       frase sem as pontuações
       
       Passos:
       1- trocar cada possível pontuação por {}
       2- substituir {} por ' '
    """
    reticencias = str.replace(frase, '...', '{}')
    ponto = str.replace(reticencias, '.', '{}')
    exclamacao = str.replace(ponto, '!', '{}')
    interrogacao = str.replace(exclamacao, '?', '{}')
    travessao = str.replace(interrogacao, '-', '{}')
    virgula = str.replace(travessao, ',', '{}')
    doispontos = str.replace(virgula, ':', '{}')
    pontovirgula = str.replace(doispontos, ';', '{}')
    espacovazio = str.replace(pontovirgula, '{}', ' ')
    
    return espacovazio
    
    return 
   
    return exclamacao + interrogacao + reticencias + ponto