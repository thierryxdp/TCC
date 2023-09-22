def retira_pontuacao(texto):
    pontuacao = '''-_,:;.'''
    nova_string=""
    for x in texto:
        if not x in pontuacao:
            nova_string=nova_string+x
        return nova_string