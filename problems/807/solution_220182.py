def conta_frases(texto):
    '''conta o número de frases de um dado texto armazenado em uma string'
   	str->int'''

    interrogaçãoViraPonto=texto.replace('?','.')

    exclamaçãoViraPonto=interrogaçãoViraPonto.replace('!','.')

    semEspacos=exclamaçãoViraPonto.replace(' ','K')
    
    return len(semEspacos.split('.'))-1