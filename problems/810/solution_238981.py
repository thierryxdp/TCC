def inverte (frase):
    """funçao que recebe uma frase de entrada e que retorna uma nova frase
    sem pontuação e que é a inversa da frase de entrada;
    string->string"""
    virgula = str.replace(frase,',','')
    travessao = str.replace(virgula,'-',' ')
    dois_pontos = str.replace(travessao,':',' ')
    ponto_virgula = str.replace(dois_pontos,';',' ')
    ponto_final = str.replace(ponto_virgula,'.',' ')
    ponto_exclamacao = str.replace(ponto_final,'!',' ')
    ponto_interrogacao = str.replace(ponto_exclamacao,'?',' ') 
    
    frase_min = str.lower(ponto_interrogacao)
    frase_sep = str.split(frase_min[:-1],' ')
    frase_nova = str.join(' ',frase_sep[::-1])

    return frase_nova