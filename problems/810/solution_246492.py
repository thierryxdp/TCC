def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     return str.split(frases , ).str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' ')
    else:
     return str.split(frases , )