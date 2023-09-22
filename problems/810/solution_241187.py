def inverte(frase):
    '''dada uma frase, retorna uma outra frase que contenha as mesmas
    palavras da frase de entrafa na ordem inversa, sem letras
    maiúsculas, e sem pontuação
    str->str'''

    removeInterrogacao=frase.replace('?','')

    removeExclamacao=removeInterrogacao.replace('!','')

    removeReticencias=removeExclamacao.replace('...','')
    
    removeVirgula=removeReticencias.replace(',','')
    
    removeDoisPontos=removeVirgula.replace(':','')
    
    removePontoVirgula=removeDoisPontos.replace(';','')
    
    removePonto=removePontoVirgula.replace('.','')
    
    travessaoViraEspaco=removePonto.replace('-',' ')

    minuscula=str.lower(travessaoViraEspaco)

    semEspaco=minuscula.strip()

    lista=semEspaco.split(' ')

    invertida=lista[::-1]

    junta=' '.join(invertida)

    return junta