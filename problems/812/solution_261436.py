def retira_pontuacao(frase):
    '''Função que retorna uma frase com os sinais de 
    pontuação substituídos por espaço; recebe como 
    parâmetro uma frase digitada pelo usuário.String-->String'''
    if('-' in frase):
        frase=str.replace(frase,'-',' ')
    if(',' in frase):
        frase=str.replace(frase,',',' ')
    if(':' in frase):
        frase=str.replace(frase,':',' ')
    if(';' in frase):
        frase=str.replace(frase,';',' ')
    if('.'in frase):
        frase=str.replace(frase,'.',' ')
    if('?' in frase):
        frase=str.replace(frase,'?',' ')
    if('!' in frase):
        frase=str.replace(frase,'!',' ')
    return frase