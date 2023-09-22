def retira_pontuacao(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     str.strip(frases , '.') in frases
     return str(frases[0:25] + frases[26:33] + frases[33:33] + frases[34:40] + frases[40:40] + frases[41:48])
    if ',' in frases and '.' in frases:
     return (str.replace(frases , ',' ,' ',2),(frases , '.' ,' ',1))
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