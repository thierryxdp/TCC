def lingua_p(Palavra):
    '''retorna Palavra traduzida para língua P
    str->str'''
    
    LetraMinuscula=Palavra.lower()
    PalavraP=''
    Vogais='aeiouáéíóúãõàì'
    
    for LinguaP in LetraMinuscula:
        PalavraP+=LinguaP
        
        if LinguaP in Vogais: