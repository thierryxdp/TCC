def retira_pontuacao(frase):
    """Substitui todas as pontuacoes da frase fornecida por espaços vazios;
    str -> str"""
    str.replace(frase, "!", " ")
    str.replace(frase, "?", " ")
    str.replace(frase, ".", " ")   
    str.replace(frase, ",", " ")    
    str.replace(frase, "-", " ")    
    str.replace(frase, ":", " ")    
    str.replace(frase, ";", " ")
    resposta = ()
    return resposta