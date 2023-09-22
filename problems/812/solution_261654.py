def retira_pontuacao (texto):
    """Retorna uma frase onde todos os caracteres de pontuação tenham sido 
    substituídos por espaço. str -> str"""
    texto1 = str.replace(texto, ',' , ' ' )
    texto2 = str.replace(texto1, texto[-1], ' ')
    #c = str.replace(texto,':',' ')
    #d = str.replace(texto,';',' ')
    
    
    return texto