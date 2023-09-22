def inverte(frase):
    '''inverte recebe uma string e devolve uma string
    inverte a ordem das palavras que aparecem anteriormente
    str --> str'''
    trav=str.replace(frase,"-","")
    vig=str.replace(trav,",","")
    doispon=str.replace(vig,":","")
    ponvig=str.replace(doispon,";","")
    pon=str.replace(ponvig,".","")
    excla=str.replace(pon,"!","")
    inter=str.replace(excla,"?","")
    esp=str.split(inter," ")
    
    return inter