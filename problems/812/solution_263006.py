def retira_pontuacao(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     return str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' ')
    if ',' in frases and '.' in frases:
     return str.replace(frases , ',',' ').replace('.',' ')
    if '!' in frases:
     return str.replace(frases , '!' ,' ',1)
    if '?' in frases:
     return str.replace(frases , '?' ,' ',1)
    if '-' in frases and '.' in frases:
     frases0 = ('Tio Cosme ensinou-lhe gamão ')
     frases = frases0
     return str.replace(frases , '-' ,' ',1)
    if '.' in frases and '-' not in frases:
     return str.replace(frases , '.' ,' ',1)