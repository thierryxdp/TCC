def retira_pontuacao:
    pontuacao = '''-_,:;.'''
    nova_string=""
    for x in myString:
        if not x in pontuacao:
            nova_string=nova_string+x
        return nova_string