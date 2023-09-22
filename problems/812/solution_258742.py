def retira_pontuacao(frase):
    lista_pares=[n for n in frase if n =='!' or n=='.' or n==';' or n==':' or n==',' or n=='-']
    f=lista_pares-frase
    return f