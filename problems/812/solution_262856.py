def retira_pontuacao(frases):
    '''f'''
    str.replace(frases , ',',' ',99)
    str.replace(frases , '.',' ',99)
    return frases