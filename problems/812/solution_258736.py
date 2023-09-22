def retira_pontuacao(frase):
    lista_pares=[n for n in frase if n =='!' ]
    lista_filtrada=''.join(lista_pares)
    return lista_filtrada