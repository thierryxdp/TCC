def retira_pontuacao(frase):
    """A função irá ter como entrada uma frase onde será retirado toda a sua pontução,
    e devolver a frase na saída sem eles.
    Entrada: String | Saída: String
    """    
    frase = frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('...', ' ').replace('.', ' ')
    return frase