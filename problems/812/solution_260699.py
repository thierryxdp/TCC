def retira_pontuacao (frase):
    """Retorna uma frase onde todos os caraceteres de espaço foram 
    sunstituídos por espaço. str->str"""
    a =str.find(frase,',')
    b =str.find(frase,'-')
    c =str.find(frase,':')
    d =str.find(frase,';')
    
    frase[a]= ' '
    frase[d]= ' '
    frase[c]= ' '
    frase[b]= ' '
    return frase