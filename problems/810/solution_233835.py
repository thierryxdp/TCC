def inverte(frase):
    '''retira_pontuacao recebe uma string e devolve uma string
    retira as pontuaçoes e coloca espaço no lugar
    str --> str'''
    trav=str.replace(frase,"-","")
    vig=str.replace(trav,",","")
    doispon=str.replace(vig,":","")
    ponvig=str.replace(doispon,";","")
    pon=str.replace(ponvig,".","")
    excla=str.replace(pon,"!","")
    inter=str.replace(excla,"?","")
    
    return inter