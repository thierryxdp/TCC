def retira_pontuacao(texto):
    '''função que substitui as pontuações em um texto, (texto), por espaço'''
    '''entrada:(texto),um texto da escolha do usuário
    saída: o texto,porém sem as pontuações'''
    if '.' in texto:
        return texto.replace('.',' ')
    if '!' in texto:
        return texto.replace('!',' ')
    if '?' in texto:
        return texto.replace('?',' ')
    if '-' in texto:
        return texto.replace('-',' ')
    if ',' in texto:
        return texto.replace(',',' ')
    if ':' in texto:
        return texto.replace(':',' ')
    if ';' in texto:
        return texto.replace(';',' ')