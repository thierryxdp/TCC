##Função que intercala duas listas  
# INT INT -->INT
def intercala(l1, l2):
    l3 =[*sum(zip(l1,l2),())]
    return l3