def retira_pontuacao(frase):
    """Substitui todas as pontuacoes da frase fornecida por espaços vazios;
    str -> str"""
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, ".", " ")   
    frase = str.replace(frase, ",", " ")    
    frase = str.replace(frase, "-", " ")    
    frase = str.replace(frase, ":", " ")    
    frase = str.replace(frase, ";", " ")
   	
    v1 = str.split(frase, " ")
    v2 = str.join(v1)
    
    return v2[::-1]