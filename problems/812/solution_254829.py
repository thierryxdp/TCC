def retira_pontuacao(frase):
    """Para retirar a pontuação da(s) frase(s), digite;
    str-> str"""
    x= frase.replace(".", "#") 
    x=frase.replace("!", "#") 
    x=frase.replace("?", " #")
    x= frase.replace(",", " #") 
    return x= frase.replace("#", " ")