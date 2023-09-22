def retira_pontuacao(frases):
    '''f'''
    if ',' in frases:
     return str.replace(frases , ',',' ',2)