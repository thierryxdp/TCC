def lingua_p(palavra):
    '''
    	Função que recebe uma palavra
        como parâmetro de entrada e 
        retorna essa palavra na língua 
        do P
        : param palavra: str
        : return: str
    '''
    palavra = str.lower(palavra)
    palavra_lingua_p = ''
    
    for letra in palavra:
        if letra in 'aáeéiíoóuú':
            palavra_lingua_p += letra + 'p' + letra  
        else:
            palavra_lingua_p += letra
    
    return palavra_lingua_p