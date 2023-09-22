def inverte(texto):
    '''funcao recebe a frase e retorna 
    ela invertida sem pontuação nenhuma
    str-> str'''
    
    if ':' in texto:
        texto= texto.replace(':' ' ')
    if '.' in texto:
        texto= texto.replace("." " ")
    if ';' in texto:
        texto= texto.replace(';' ' ')
    if '?' in texto:
        texto= texto.replace('?' ' ')
    if '!' in texto: 
        texto= texto.replace('!' ' ')
    if ',' in texto:
        texto= texto.replace(',' ' ')
        
    textolist= texto.reverse(texto) 
    return textolist