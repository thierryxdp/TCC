def posLetra(frase,letra,ocorrencia):
    '''função que retorna a ordem da ocorrencia da letra indicada na frase;
    str,str->int'''
    ocorreu= frase.find(letra)
    while ocorreu>=1 and ocorrencia>1:
        ocorreu= frase.find(letra,ocorreu+1)
        ocorrencia-=1
    return ocorreu