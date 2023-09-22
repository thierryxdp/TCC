def retiraPontuacao(frase):
    '''Função que, dada uma frase como entrada, substitui todos os caracteres de pontuação por espaços em branco; str->str'''
    
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'?',' ')
    return frase

def inverte (texto):
    '''Função que, dada uma frase, retorna uma nova frase contendo as mesmas 
    palavras em ordem inversa, sem letras maiúsculas e sem pontuação;
    str->str'''
    
    texto= retira_pontuacao(texto)
    texto=str.lower(texto)
    texto=str.split(texto)
    texto_inverso=texto[::-1]
    return str.join(" ",texto_inverso)