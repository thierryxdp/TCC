def conta_frases(texto):
    '''conta o número de frases de um dado texto armazenado em uma string'
   	str->int'''

    interrogacaoViraPonto=texto.replace('?','.')

    exclamacaoViraPonto=interrogacaoViraPonto.replace('!','.')

    reticenciasViraPonto=exclamacaoViraPonto.replace('...','.')

    semEspacos=reticenciasViraPonto.replace(' ','K')
    
    return len(semEspacos.split('.'))-1