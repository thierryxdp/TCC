def inverte(string):
    """Ao fornecer uma frase, retirar a pontuação presente e substituí-la por espaço em branco. Posteriormente inverter a ordem das palavras e reagrupar as palavras em uma frase
    str -> str"""
    
    string = string.replace(',', '')    # retirar pontuação
    string = string.replace('-', ' ')    #
    string = string.replace(':', '')    #
    string = string.replace('.', '')    #   
    string = string.replace(';', '')    #
    string = string.replace('?', '')    #
    string = string.replace('!', '')    #

    string = str.lower(string)          # transformar frase em minúscula
    
    string = string.split(' ')          # separar palavras em lista

    string = string[::-1]               # inverter ordem da lista

    string = str.join(' ', string)      # reagrupar palavras

    return string