def lingua_p(P):
    """Funcao que recebe como parametro uma palavra P
    (em portugues) e retorna esta mesma palavra traduzida 
    para a lingua do P. Uma palavra foi traduzida para a 
    lingua do P quando, apos cada vogal da palavra original,
    e inserida a sequencia de letras 'p' mais a vogal
    original. A resposta ignora a diferenca entre minusculas
    e maiusculas e retorna a palavra traduzida toda em 
    minusculas;
    str->str"""
    
    Pminuscula=str.lower(P)
    Ptraduzida=''
    
    for letra in Pminuscula:
        if letra not in 'bcdfghjklmnpqrstvwxyzç':
            letra=letra+'p'+letra
        Ptraduzida=Ptraduzida+letra
    return Ptraduzida