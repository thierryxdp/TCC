def retira_pontuacao(frase1):
    '''Retira toda e qualquer pontuação da frase cadastrada;
    str -> str'''
    frase_nova = frase1
    frase_nova = str.replace(frase_nova,'...',' ')
    frase_nova = str.replace(frase_nova,'.',' ')
    frase_nova = str.replace(frase_nova,';',' ')
    frase_nova = str.replace(frase_nova,'!',' ')
    frase_nova = str.replace(frase_nova,'?',' ')
    frase_nova = str.replace(frase_nova,':',' ')
    frase_nova = str.replace(frase_nova,',',' ')
    frase_nova = str.replace(frase_nova,'-',' ')
    frase_nova = str.replace(frase_nova,';',' ')
    return frase_nova
def inverte(frase2):
    '''Inverte a frase cadastrada sem pontuacao;
    str -> str'''
    frase_inv = str.lower(str.strip(retira_pontuacao(frase2)))
    frase_inv = str(str.split(frase_inv))
    return frase_inv[::-1]