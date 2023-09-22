def retira_pontuacao(frase):
    """Dada uma frase, a função vai substituir todos caracteres
    de pontuação(exclamação, interrogação, reticências, ponto final,
    dois pontos, vírgula, ponto e vírgula ou travessão) por um caractere
    de espaço.
    A frase deve ser escrita entre aspas;
    str --> str"""
    frase = frase.replace("!","/")
    frase = frase.replace("?","/")
    frase = frase.replace("...","/")
    frase = frase.replace(".","/")
    frase = frase.replace(":","/")
    frase = frase.replace(",","/")
    frase = frase.replace(";","/")
    frase = frase.replace("-","/")
    frase = frase.split("/")
    frase = " ".join(frase)
    return frase