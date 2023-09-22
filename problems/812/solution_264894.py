def retira_pontuacao(frase):
    '''
    
    '''
    subst_travessao = str.replace((frase), '-', ' ')
    subst_virgula = str.replace((frase), ',', ' ')
    subst_dois_pontos = str.replace((frase), ':', ' ')
    subst_ponto_e_virgula = str.replace((frase), ';', ' ')
    subst_encerramento = str.replace((frase), '.', ' ')
    
    return subst_travessao + subst_virgula + subst_dois_pontos + subst_ponto_e_virgula + subst_encerramento