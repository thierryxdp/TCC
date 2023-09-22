def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     return invert(str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' '))