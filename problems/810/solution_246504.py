def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     frases0 = (str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' '))
     frases1 = (str.split(frases0, ))
     frases2 = frases1[::-1]
    if len(frases2) == 8:
     return  str.lower(str(frases2[0]) + ' ' + str(frases2[1]) + ' ' + str(frases2[2])+' ' + str(frases2[3])+' ' +str(frases2[4])+' ' + str(frases2[5])+ ' ' + str(frases2[6])+ ' ' + str(frases2[7]))
    if len(frases2) > 8:
     return  str.lower(str(frases2[0]) + ' ' + str(frases2[1]) + ' ' + str(frases2[2])+' ' + str(frases2[3])+' ' +str(frases2[4])+' ' + str(frases2[5])+ ' ' + str(frases2[6])+ ' ' + str(frases2[7])+' '+ str(frases2[8])+' '+ str(frases2[9]) + ' ' + str(frases2[10])+' ' + str(frases2[11])+' ' +str(frases2[12])+' ' + str(frases2[13])+ ' ' + str(frases2[14])+ ' ' + str(frases2[15]))
    else:
     return str.split(frases , )