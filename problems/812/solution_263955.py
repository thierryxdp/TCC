def retira_pontuacao(frase):
    """troca toda pontuaçao de uma frase por espaço"""
    
    a=frase.replace("!"," ")
    
    b=a.replace("-"," ")
    
    c=b.replace(","," ")
    
    d=c.replace("."," ")
    
    return d