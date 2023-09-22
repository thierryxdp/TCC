def inverte(frase):
    '''Função que, dada um frase, retorna ela na ordem inversa, sem letras maiúsculas e sem pontuação.7
    str --> str'''
    texto_espacado = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'...',' '),',',' '),'-',' '),'!',' '),'?',' '),'.',' '),';',' '),':',' ')
    separada_invertida = str.split(sem_pontuação)[::-1]
    juntando = str.join(' ',separada_invertida)
    final = str.lower(juntando)
    return final