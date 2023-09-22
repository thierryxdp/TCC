def retira_pontuacao(frases):
    '''f'''
    if '.' in frases and '-' not in frases:
     return str.replace(frases , '.' ,' ',1)
    if '!' in frases:
     return str.replace(frases , '!' ,' ',1)
    if '?' in frases:
     return str.replace(frases , '?' ,' ',1)
    if '-' and '.' in frases:
     return str.replace(frases , '-' ,' ',1)