def inverte(frase):
    '''funcao que dado uma frase retorna essa mesma frase na ordem inversa
    e sem nenhuma pontuacao; str -> str'''
    lista = str.split(frase)
    inverter = lista[::-1]
    nova_frase = str.join(inverter)
    
    retira = str.replace(nova_frase,'.',',')
    retira2 = str.replace(retira,',','-')
    retira3 = str.replace(retira2,'-',';')
    retira4 = str.replace(retira3,';',':')
    retira5 = str.replace(retira4,':','?')
    retira6 = str.replace(retira5,'?','!')
    retira7 = str.replace(retira6,'!',' ')
    frase_final = retira7
    
    return frase_final