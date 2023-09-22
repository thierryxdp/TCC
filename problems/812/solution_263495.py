def retira_pontuacao(x):
    '''retira a pontuação presente em uma frase'''
    caracteres='-,:;?!.'
    frase=str()
    if '-' in x:
        frase=x.replace(caracteres[0],'')
    if ',' in x:
        frase=x.replace(caracteres[1],'')
    if ':' in x:
        frase=x.replace(caracteres[2],'')
    if ';' in x:
        frase=x.replace(caracteres[3],'')
    if '?' in x:
        frase=x.replace(caracteres[4],'')
    if '!' in x:
        frase=x.replace(caracteres[5],'')
    if '.' in x:
        frase=x.replace(caracteres[6],'')
    
    return frase