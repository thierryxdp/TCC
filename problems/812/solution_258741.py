def retira_pontuacao(frase):
    lista_pares=[n for n in frase if n =='!' or n=='.' or n==';' or n==':' or n==',' or n=='-']
    lista_filtrada=(''.join(frase))
    return lista_pares