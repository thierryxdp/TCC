def uppCons(texto):
    '''Retorna a frase de entrada com todas as consoantes em msiúsculas, str ->str'''
    lista=list(texto)
    i=0
    nova=[]
    while i<len(lista):
        if lista[i]not in 'AEIOUaeiouáéíóúÁÉÍÓÚàÀãõÃÕâêîôûÂÊÎÔÛ':
            nova=nova+list(str.upper(texto[i]))
            i=i+1
        else:
            nova = nova + list(texto[i])
            i=i+1
    return str.join('',nova)