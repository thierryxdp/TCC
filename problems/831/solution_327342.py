def lingua_p(palavra):
    '''Função que dada uma palavra retorna a mesma palavra 
    na língua do p (p+vogal depois de toda vogal da palavra)
    str->str'''
    palavra_minusculo= str.lower(palavra)
    palavra_nova=''
    vogais='aeiouáéíóú'
    letra_p='p'
    
    for i in range(len(palavra_minusculo)):
        if palavra_minusculo[i] in vogais:
            palavra_nova=palavra_nova+palavra_minusculo[i]+letra_p+palavra_minusculo[i]
            
        else:
            palavra_nova=palavra_nova+palavra_minusculo[i]
            
    return palavra_nova