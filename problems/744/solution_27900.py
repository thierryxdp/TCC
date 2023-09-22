#---------------------EXERCICIO 4---------------------

def hastag (texto):
    '''Retorna o texto com # no meio
    str ->str'''
    tamanhoTexto = len(texto)
    if (tamanhoTexto%2)==0:
        textofatiado1=texto[:int((tamanhoTexto/2))]
        textofatiado2=texto[(len(textofatiado1)):]
    else:
        textofatiado1=texto[:((tamanhoTexto//2))]
        textofatiado2=texto[(len(textofatiado1)):]
    textonovo='#'+textofatiado1+'#'+textofatiado2+'#'
    return textonovo