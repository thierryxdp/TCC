def inverte(frase):
    ''' essa função retira todas as pontuações existente na frase, str,str,str'''
    conta = str.join(' ', str.split(frase, '.'))
    cont1 = str.join(' ', str.split(conta, ','))
    cont2 = str.join(' ', str.split(cont1, '!'))
    cont3 = str.join(' ', str.split(cont2, '?'))
    cont4 = str.join(' ', str.split(cont3, '-'))
    cont5 = str.split(cont4)
    
    
    return ((str.lower(cont5))[::-1])