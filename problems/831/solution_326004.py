def lingua_p(palavra):
    """Função que traduz uma palavra escrita em português, para ela
    mesma escrita na lingua do P.
    Entrada: str;
    Saida: str;
    
    Parameter:
    palavra: Palavra para ser traduzida.
    """
    palavra = palavra.lower()
    nova_Palavra = ''
    
    for letra in palavra:
        if letra in "aeiouáéíóúàèìòùâêîôûãõ":
            nova_Palavra += letra + "p" + letra
        else:
            nova_Palavra += letra
            
    return nova_Palavra