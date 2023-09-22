def lingua_p(palavra):
    '''Função que insere na string de entrada (palavra) o caractere p após cada
    vogal da string, é a função para escrita na língua do p.
    Entrada: str. Saída: str.'''
    palavra=str.lower(palavra)
    string=''
    for caracter in palavra:
        if caracter in 'aeiouáéíóúãõâêîôû': 
            string=string+caracter+'p'+caracter
        else:
            string=string+caracter
    return string