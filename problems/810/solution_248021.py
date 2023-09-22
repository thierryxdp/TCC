def inverte(frase):  
    def retira_pontuacao(frase):
    ''' funcao que recebe uma string e retorna a string sem os sinais de pontuacao; str-> str'''
    frase=frase.replace(',','.')
    frase=frase.replace('?', '.')
    frase=frase.replace('!','.')
    frase=frase.replace('-','.')
    
    return frase.replace('.',' ')
    

    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase