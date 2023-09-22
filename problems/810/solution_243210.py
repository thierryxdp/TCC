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
def inverte(frase):
    '''Função que retorna uma frase sem pontuações,
    sem letras maíusculas e invertida.String-->String'''
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    return str.join(' ',list.reverse(str.split(frase)))