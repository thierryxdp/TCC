def inverte(frase):
    frase.replace('!',' ')
    #Aqui ele vai substituir todas as ocorrÊncias de '!' por ' '
    frase=frase.replace('...',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('_',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    return frase