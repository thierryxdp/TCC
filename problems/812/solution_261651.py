def retira_pontuacao (texto):
    """Retorna uma frase onde todos os caracteres de pontuação tenham sido 
    substituídos por espaço. str -> str"""
    a = (str.replace(texto, ',' , ' ' ))
    #b = str.replace(texto,'-',' ')
    #c = str.replace(texto,':',' ')
    #d = str.replace(texto,';',' ')
    
    
    return a