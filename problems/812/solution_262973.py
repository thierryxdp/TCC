def retira_pontuacao(frase):
    '''Esta e a funcao que dada uma frase, retorna
    a frase onde todos os caracteres de pontuacao são 
    substituidos por espaco
    str -> str'''
    tamanho_da_frase=len(frase)
    copia_da_frase=list(frase)
    for indice in range(0,tamanho_da_frase):
        if frase[indice]=='?':
            copia_da_frase[indice]=''
        if frase[indice]=='!':
            copia_da_frase[indice]=''
        if frase[indice]=='.':
            copia_da_frase[indice]=''
        if frase[indice]==',':
            copia_da_frase[indice]=''
        if frase[indice]=='-':
            copia_da_frase[indice]=''
        if frase[indice]==':':
            copia_da_frase[indice]=''
        if frase[indice]==';':
            copia_da_frase[indice]=''
        nova_frase=''.join(copia_da_frase)
        return(nova_frase)