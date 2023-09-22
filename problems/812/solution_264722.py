def retira_pontuacao(string):
    ''' funcao que dada uma frase de entrada substitui os pontos das frases por espaços em branco 
        str --> str '''
    
    retira_ponto_final = str.replace(string,'.',' ')
    retira_ponto_interrogacao = str.replace(string,'?',' ')
    retira_ponto_exclamacao = str.replace(string,'!',' ')
    retira_virgula = str.replace(string,',',' ')
    retira_travessao = str.replace(string,'-',' ')
    retira_dois_pontos = str.replace(string,':',' ')
    retira_ponto_virgula = str.replace(string,';',' ')
    
    return retira_ponto_final + retira_ponto_interrogacao + retira_ponto_exclamacao + retira_virgula + retira_travessao + retira_dois_pontos + retira_ponto_virgula