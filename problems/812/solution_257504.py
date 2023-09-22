def retirar(frase):
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    return frase

def retira_pontuacao(frase):
    frase = list(frase)
    frase = map(retirar,frase)
    
    resp =''
    for i in range(len(frase)):
        resp+=str(frase[i])
    return f=resp