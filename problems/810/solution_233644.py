def inverte(frase):
    '''funcao que dado uma frase retorna essa mesma frase na ordem 
    inversa e sem nenhuma pontuacao; str -> str'''
    
    retira1 = str.replace(frase,'.','-')
    retira2 = str.replace(retira1,'-',',')
    retira3 = str.replace(retira2,',',';')
    retira4 = str.replace(retira3,';',':')
    retira5 = str.replace(retira4,':','?')
    retira6 = str.replace(retira5,'?','!')
    retira7 = str.replace(retira6,'!',' ')
    frase2= str.lower(retira7)
    
    lista = str.split(frase2)
    inverter = lista[::-1]
    frase_final = str.join(' ',inverter)
    
    return frase_final