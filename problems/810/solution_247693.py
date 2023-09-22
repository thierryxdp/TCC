def inverte(frase):
    ''' essa função retira todas as pontuações existente na frase, str,str,str'''
    frase1 = str.lower(frase)
    conta = str.join(' ', str.split(frase1, '.'))
    cont1 = str.join(' ', str.split(conta, ','))
    cont2 = str.join(' ', str.split(cont1, '!'))
    cont3 = str.join(' ', str.split(cont2, '?'))
    cont4 = str.join(' ', str.split(cont3, '-'))
   
    
    
    return cont4