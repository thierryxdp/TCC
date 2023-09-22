def posletra(string,letra,numero):
    '''Calcula e retorna em qual posiçao de uma string a letra determinada aparace a partir do seu numero de ocorrencia
       parameters:
       string: uma string qualquer, seja ela texto, palavra..
       letra: letra qualquer do alfabeto
       numero: numero da ocorrenciia de uma letra
       str,str,int->int'''
    posicao=0
    ocorrencia=0
    while posicao < len(string):
        if string.count(letra)<numero:
            ocorrencia= ocorrencia - 1
    return ocorrencia