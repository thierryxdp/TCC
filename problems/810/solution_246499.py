def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     frases0 = (str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' '))
     frases1 = (str.split(frases0, ))
     frases2 = frases1[::-1]
     return str(frases2[0]) + str(frases2[1]) + str(frases2[2]) + str(frases2[3]) +str(frases2[4]) + str(frases2[5]) + str(frases2[6]) + str(frases2[7]) 
    else:
     return str.split(frases , )