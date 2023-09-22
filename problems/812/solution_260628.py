def retira_pontuacao(frase):
    """Atribui a frase recebida a outra variável e modifica esta última,
    substituindo toda pontuação por espaços.
    str-> str"""
    frase_nova=frase
    frase_nova=frase_nova.replace("..."," ")
    frase_nova=frase_nova.replace("."," ")
    frase_nova=frase_nova.replace("!"," ")
    frase_nova=frase_nova.replace("?"," ")
    frase_nova=frase_nova.replace("-"," ")
    frase_nova=frase_nova.replace("-"," ")
    frase_nova=frase_nova.replace(","," ")
    frase_nova=frase_nova.replace(":"," ")
    frase_nova=frase_nova.replace(";"," ")
    return frase_nova