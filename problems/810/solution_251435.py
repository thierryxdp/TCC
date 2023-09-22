def retira_pontuacao(frase):#funcao reutilizada do exercicio anterior
    '''funcao que retira a pontuacao de um texto str->str'''
    retira1 = (str.replace(frase, '!', ' '))
    
    retira2 = (str.replace(retira1, '.', ' '))
    
    retira3 = (str.replace(retira2, '?', ' '))
    
    retira4 = (str.replace(retira3, ',', ' '))
    
    retira5 = (str.replace(retira4, '-', ' '))
    
    retira6 = (str.replace(retira5, ',', ' '))
    
    retira7 = (str.replace(retira6, ':', ' '))
    
    retira8 = (str.replace(retira7, ';', ' '))
    
    return retira8

def inverte(frase):
    '''funcao que inverte as palavras de uma frase'''
    passo1 = retira_pontuacao(frase)
    
    passo2 = str.lower(passo1)
    
    lista = str.split(passo2)
    
    lista.reverse()
    
    return str.join('',lista)