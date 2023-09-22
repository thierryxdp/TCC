def lingua_p(palavra):
    """FUNÇÃO QUE RETORNA UMA PALAVRA TRADUZIDA 
    PARA A LINGUA DO P
    STR=>STR"""
    palavra.lower()
    palavraF=' '
    
    for i in palavra:
        if i in 'áéíóúaeiou':
            palavraF += i+'p'+i
        else:
            palavraF += i
    return palavraF.lstrip()