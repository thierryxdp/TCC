def inverte(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço. E inverte a função no final'''
    ''' Entrada = string ; saída = string '''
    pontuacao = '.'
    frase = str.replace(texto,pontuacao,'')
    pontuacao1= ','
    frase1 = str.replace(frase,pontuacao1,'')
    pontuacao2= ';'
    frase2 = str.replace(frase1,pontuacao2,'')
    pontuacao3=':'
    frase3 = str.replace(frase2,pontuacao3,'')
    pontuacao4='-'
    frase4 = str.replace(frase3,pontuacao4,'')
    pontuacao5 = '?'
    frase5 = str.replace(frase4,pontuacao5,'')
    pontuacao6 = '!'
    frase6 = str.replace(frase5,pontuacao6,'')
    nova_frase = frase6[-1:]
    return nova_frase