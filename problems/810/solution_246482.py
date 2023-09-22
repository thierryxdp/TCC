def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     return list.reverse(str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' '))