def retira_pontuacao(frase):
    '''retira os sinais de pontuaçao de uma frase e retorna uma frase nova com espaços no lugar
       parameters:
       frase: uma frase qualquer que sera alterada
       str-> str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'?',' ')
    return frase