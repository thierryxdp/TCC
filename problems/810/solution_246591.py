def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     frases0 = (str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' '))
     frases1 = (str.split(frases0, ))
     frases2 = frases1[::-1]
     Strfrases2 = " ".join(frases2)
     return str.lower(Strfrases2)
    if ',' in frases and '.' in frases:
     frases0 = (str.replace(frases , ',' , ' ').replace('.',' '))
     frases1 = (str.split(frases0, ))
     frases2 = frases1[::-1]
     Strfrases2 = " ".join(frases2)
     return str.lower(Strfrases2)
    if '!' in frases:
     frases0 = (str.replace(frases , '!' , ' '))
     frases1 = (str.split(frases0, ))
     frases2 = frases1[::-1]
     Strfrases2 = str.join('',frases2)
     return str.lower(Strfrases2)