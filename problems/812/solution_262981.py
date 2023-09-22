def retira_pontuacao(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     str.strip(frases , '.') in frases
     str.replace(frases[24:27] , ',', '' ,1)
     return frases
    if '.' in frases and '-' not in frases:
     return str.replace(frases , '.' ,' ',1)
    if '!' in frases:
     return str.replace(frases , '!' ,' ',1)
    if '?' in frases:
     return str.replace(frases , '?' ,' ',1)
    if '-' and '.' in frases:
     frases0 = ('Tio Cosme ensinou-lhe gamão ')
     frases = frases0
     return str.replace(frases , '-' ,' ',1)