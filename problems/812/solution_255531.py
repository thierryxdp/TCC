def retira_pontuacao(s):
    """dada uma frase,retorna a frase sendo que todos os caracteres de pontuação são substituídos por espaço"""
    l1=str.replace(s,"?","")
    l2=str.replace(l1,"!","")
    l3=str.replace(l2,".","")
    l4=str.replace(l3,",","")
    l5=str.replace(l4,";","")
    l6=str.replace(l5,":","")
    l7=str.replace(l6,"-","")
    return l7