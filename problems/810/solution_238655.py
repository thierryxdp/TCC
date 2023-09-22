def inverte(frase):
    '''funcao que dada uma frase, retorne esta mesma, mas, sem letras maiusculas,sem pontuacao, 
    substituindo isso por espaco e retornando a frase na ordem inversa. str->str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    
    frase= str.lower(frase)
    frase=str.split(frase)
    frase= frase[::-1]
    
    return str.join(' ',frase)