def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     frases0 = (str.replace(frases , ',' , ' ').replace('-',' ').replace('.',' '))
     frases4 =  str.replace(frases0 ,'  ', '7 ', 99999)
     frases1 = (str.split(frases4, ))
     frases2 = frases1[::-1]
     return  str.replace(str(frases2[0]) + ' ' + str(frases2[1]) + ' ' + str(frases2[2])+' ' + str(frases2[3])+' ' +str(frases2[4])+' ' + str(frases2[5])+ ' ' + str(frases2[6])+ ' ' + str(frases2[7]) + ' ', '7',' ',9999)
    else:
     return str.split(frases , )