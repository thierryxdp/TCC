def retira_pontuacao(frase):
    ''' funcao que recebe uma string e retorna a string sem os sinais de pontuacao; str-> str'''
    frase=frase.replace(',','.')
    frase=frase.replace('?', '.')
    frase=frase.replace('!','.')
    frase=frase.replace('-','.')
    
    return frase.replace('.',' ')
    
def inverte(frase):  
    lista = str.split(frase)
    lista.reverse()
    #lista = list.reverse(lista)
    frase = str.join(" ", lista)
    return frase