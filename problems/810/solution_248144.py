def inverte(frase):  
    ''' funcao que recebe ua string e retorna a string invertida sem o sinais de pontuacao; str-> str'''
    frase=frase.replace(',','.')
    frase=frase.replace('?', '.')
    frase=frase.replace('!','.')
    frase=frase.replace('-','.')
    frase=frase.replace('.', ' ') 
        
        lista = str.split(frase)
        lista.reverse()
        frase = str.join(' ' ,lista)
        frase= frase.lower()
        return frase