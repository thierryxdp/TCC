def retira_pontuacao(string):
    ''' funcao que dada uma frase de entrada substitui os pontos das frases por espaços em branco 
        str --> str '''
    
    retira_ponto_final = str.replace(string,'.',' ')
    retira_ponto_interrogacao = str.replace(string,'?',' ')
    retira_ponto_exclamacao = str.replace(string,'!',' ')
    retira_virgula = str.replace(string,',',' ')
    retira_travessao = str.replace(string,'-',' ')
    
    if '?' in string:
        return retira_ponto_interrogacao
    
    if '!' in string:
        if '-' in string:
            return str.replace(retira_travessao,'!',' ')
        else:
            return retira_ponto_exclamacao
    
    if '.' in string:
        if (',' in string) and ('-' in string):
            resultado1 = retira_virgula
            resultado2 = str.replace(resultado1,'-',' ')
            resultado3 = str.replace(resultado2,'.',' ')
            return resultado3
        elif ',' in string:
            return str.replace(retira_virgula,'.',' ')
        elif '-' in string:
            return str.replace(retira_travessao,'.',' ')
        else:
            return retira_ponto_final