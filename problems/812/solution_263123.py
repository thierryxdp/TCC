def retira_pontuacao(frase):
     lista = [frase]
    for n, i in enumerate(lista):
        if i == '.' or ',' or '!' or '?' or '-' or ';' or ':':
         lista[n] = ' '
    return print(lista)