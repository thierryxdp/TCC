def lingua_p(palavra):
    '''A função recebe uma palavra (em português) e retorna essa palavra traduzida para
    a língua do P.
    Parâmetro de entrada: str
    Valor de retorno: str'''
    palavra=str.lower(palavra)
    palavra_traduzida=''
    for caractere in palavra:
        if caractere in 'aeiouáéíóúâêô':
            caractere=caractere+'p'+caractere
        palavra_traduzida=palavra_traduzida+caractere
    return palavra_traduzida