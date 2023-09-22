def retirar(frase):
    if frase in '-,:.!? ':
        frase =' '
    return frase

def retira_pontuacao(frase):
    frase = list(map(retirar,frase))
    
    resp =''
    for i in range(len(frase)):
        resp+=str(frase[i])
    return resp