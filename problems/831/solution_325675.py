def lingua_p(palavra):
    """funcao que retorna uma palavra em portugues traduzida para a lingua do p;
    str -> str"""

    palavra_p = ''

    for termo in palavra:

        if termo in 'AEIOUaeiouáéíóúãõâêîôû':
            palavra_p += termo + 'p' + termo

        else:
            palavra_p += termo
            


    return str.lower(palavra_p)