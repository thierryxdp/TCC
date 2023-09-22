def retira_pontuacao(frase):
    """Dado uma frase, retorna a frase onde todas as pontuacoes sao substituidas por espaco"""
    frase=frase.replace("-"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("."," ")
    return frase