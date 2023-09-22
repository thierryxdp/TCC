def retira_pontuacao(frase):
    '''Função que recebe uma string e substitui sua 
    pontuação por espaços
    str->str'''
    if "." in frase:
        frase = frase.replace("."," ")
    if "!" in frase:
        frase = frase.replace("!"," ")
    if "?" in frase:
        frase = frase.replace("?"," ")
    if "..." in frase:
        frase = frase.replace("..."," ")
    if "," in frase:
        frase = frase.replace(","," ")
    if "-" in frase:
        frase = frase.replace("-"," ")
    return frase
def inverte(frase):
    '''Essa funçao recebe uma frase, remova sua pontuação
    e a inverte
    str->str'''
    frase = retira_pontuacao(frase)
    frase=frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return (frase)