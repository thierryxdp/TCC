def retira_pontuacao(frase):
    '''
    Funçao que dada uma frase, a retorna com todos os caracteres de
    pontuaçao substituidos por espaço
    str -> str
    '''
    trav= str.replace(frase,'-',' ')
    virg= str.replace(frase,',',' ')
    dois= str.replace(frase,':',' ')
    pon_v= str.replace(frase,';',' ')
    final= str.replace(frase,'.',' ')