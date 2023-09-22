def inverte(frase):
    '''dada uma frase, retorna uma outra frase que contenha as mesmas
    palavras da frase de entrafa na ordem inversa, sem letras
    maiúsculas, e sem pontuação
    str->str'''

    removeInterrogacao=frase.replace('?','')

    removeExclamacao=removeInterrogacao.replace('!','')

    removeReticencias=removeExclamacao.replace('...','')

    removeTravessao=removeReticencias.replace('-','')
    
    removeVirgula=removeTravessao.replace(',','')
    
    removeDoisPontos=removeVirgula.replace(':','')
    
    removePontoVirgula=removeDoisPontos.replace(';','')
    
    removePonto=removePontoVirgula.replace('.','')

    lista=str.split(removePonto,' ')

    inversa=lista[::-1]

    return str.lower(str.join(' ',inversa))