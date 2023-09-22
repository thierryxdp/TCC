def retira_pontuacao (frase):
    """Retorna uma frase onde todos os caraceteres de espaço foram 
    sunstituídos por espaço. str->str"""
    a = str.replace(frase,',',' ') and or str.replace(frase,'-',' ') and or str.replace(frase,':',' ') and or str.replace(frase,';',' ')
    return a