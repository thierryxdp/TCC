def retira_pontuacao(frase):
    """Coloque um comentário dizendo o que a função faz e quais são 
    os parâmetros de entrada e saída
    str-> int"""
    x= frase.replace(".", "#") 
    y=frase.replace("!", "#") 
    z=frase.replace("?", " #")
    a= frase.replace(",", " #") 
    return frase.replace("#","")