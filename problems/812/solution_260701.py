def retira_pontuacao (frase):
    """Retorna uma frase onde todos os caraceteres de espaço foram 
    sunstituídos por espaço. str->str"""
    a =str.find(frase,',')
    b =str.find(frase,'-')
    c =str.find(frase,':')
    d =str.find(frase,';')
    
    frase2=frase[:]
    frase2[a]= ' '
    frase2[d]= ' '
    frase2[c]= ' '
    frase2[b]= ' '
    return frase