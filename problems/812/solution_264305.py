def retira_pontuacao(frase):
    if '.' in frase:
        print (frase.replace('.', ' '))
    elif '-' in frase:
        print (frase.replace('-', ' '))
    elif ',' in frase:
        print (frase.replace(',',' '))
    elif ':' in frase:
        print (frase.replace(':', ' '))
    elif ';' in frase:
        print (frase.replace(';', ' '))