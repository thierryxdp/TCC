def substitui(frase):
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

def inverte(frase):
    fras=substitui(frase)
    fras= fras[0].lower() + fras[1:]
    fras=fras.split(' ')
    fras.reverse()
    fras=' '.join(fras)
    return fras