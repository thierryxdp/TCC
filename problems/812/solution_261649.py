def retira_pontuacao (texto):
    """Retorna uma frase onde todos os caracteres de pontuação tenham sido 
    substituídos por espaço. str -> str"""
    a = (str.replace(texto,',',' ')) and (str.replace(texto,texto[-1],' ')) 
    #b = str.replace(texto,'-',' ')
    #c = str.replace(texto,':',' ')
    #d = str.replace(texto,';',' ')
    
    
    return a