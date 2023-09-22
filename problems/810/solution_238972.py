def inverte (frase):
    """funçao que recebe uma frase de entrada e que retorna uma nova frase
    sem pontuação e que é a inversa da frase de entrada;
    string->string"""
    
    frase_min = str.lower(frase)
    frase_sep = str.split(import.retira_pontuacao(frase_min),' ')
    frase_nova = str.join(' ',frase_sep[::-1])

    return frase_nova