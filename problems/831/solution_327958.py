def lingua_p(palavra):
    """função que retorna a palavra de entrada em português traduzida para a lingua do p;
    Entrada: str
    Saída: str"""
    resultado = []
    
    for letra in palavra:
        str.lower(letra)
        if letra in 'aeiouãõáéíóúâêîôû':
            x = letra + 'p' + letra
        	list.append(resultado,x)
        else:
        	list.append(resultado,letra)
    return str.join('',resultado)