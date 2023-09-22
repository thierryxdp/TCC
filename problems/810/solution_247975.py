def inverte(t):
    ''
    txt= t.replace('?','')
    txt2= txt.replace('!','')
    txt3= txt2.replace('.','')
    txt4= txt3.replace('...','')
    txt5= txt4.replace(':','')
    txt6= txt5.replace(';','')
    txt7= txt6.replace('/','')
    txt8= txt7.replace(',','')
    txt9= txt8.replace('-','')
    T= str.lower(txt9)
    T2= T.split(' ')
    T3= list.reverse(T2)
    return T3