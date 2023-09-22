def retira_pontuacao(frase):
    '''retorna a frase onde todos os 
    caracteres de pontuação tenham sido substituídos por espaço
    dada uma frase
    str->str'''

    interrogacaoViraEspaco=frase.replace('?',' ')

    exclamacaoViraEspaco=interrogacaoViraEspaco.replace('!',' ')

    reticenciasViraEspaco=exclamacaoViraEspaco.replace('...',' ')

    travessaoViraEspaco=reticenciasViraEspaco.replace('-',' ')
    
    virgulaViraEspaco=travessaoViraEspaco.replace(',',' ')
    
    doisPontosViraEspaco=virgulaViraEspaco.replace(':',' ')
    
    pontoVirgulaViraEspaco=doisPontosViraEspaco.replace(';',' ')
    
    pontoViraEspaco=pontoVirgulaViraEspaco.replace('.',' ')
    
    return pontoViraEspaco