def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     frases0 = (str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' '))
     frases1 = (str.split(frases0, ))
     frases2 = (list.reverse(frases1))
     return (frases2)
    else:
     return str.split(frases , )