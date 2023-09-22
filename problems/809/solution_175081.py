# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''teste'''
    lista3= lista1+lista2
    
    ind1=str(lista3[0])
    ind2=str(lista3[1])
    ind3=str(lista3[2])
    ind4=str(lista3[3])
    ind5=str(lista3[4])
    ind6=str(lista3[5])
    
    lista4=(ind1+ind2+ind3+ind4+ind5+ind6)
    
    return str.replace(str.replace(str.replace(lista4,str(ind1),str(ind4)),str(ind2),str(ind5)),str(ind3),str(ind6))