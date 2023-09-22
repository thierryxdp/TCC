def retira_pontuacao(texto):
    '''funcao que dado um texto retira toda a sua pontuacao
    str->str'''
    x=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,':','#'),';','#'),',','#'),'-','#'),'.','#'),'!','#'),'?','#')
    return str.replace(x,'#',' ')