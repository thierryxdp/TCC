def retira_pontuacao(frase):
    '''Retorna uma frase onde todos os caracteres de pontuação 
    são substituídos por espaço
    str->str'''
    passo_a_passo=str.replace(frase,'-',' ')
    passo_a_passo=str.replace(passo_a_passo,',','')
    passo_a_passo=str.replace(passo_a_passo,':','')
    passo_a_passo=str.replace(passo_a_passo,';','')
    passo_a_passo=str.replace(passo_a_passo,'.','')
    passo_a_passo=str.replace(passo_a_passo,'!','')
    passo_a_passo=str.replace(passo_a_passo,'?','')
    return passo_a_passo


def inverte(frase):
    '''Retorna uma nova frase que é o inverso da frase de entrada
    str->str'''
    
    nova_frase=retira_pontuacao(frase)
    lista=str.split(nova_fase)
    list.reverse(lista)
    
    return lista