def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     return str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' ')