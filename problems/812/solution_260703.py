def retira_pontuacao (frase):
    """Retorna uma frase onde todos os caraceteres de espaço foram 
    sunstituídos por espaço. str->str"""
    a =str.find(frase,',')
    b =str.find(frase,'-')
    c =str.find(frase,':')
    d =str.find(frase,';')
    
    frase2=list(frase[:])
    frase2[0][a]= ' '
    frase2[0][d]= ' '
    frase2[0][c]= ' '
    frase2[0][b]= ' '
    return str(frase2)