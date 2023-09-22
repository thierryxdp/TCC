def retira_pontuacao(f):
    'recebe uma frase e substitui suas pontuações por espaço'
    'entrada: str'
    'saida: str'
    nova=''
    if '-' in f:
        nova=str.replace(f,'-',' ')
    if ',' in nova:
        nova=str.replace(nova,',',' ')
    if ':' in nova:
        nova=str.replace(nova,':',' ')
    if ';' in nova:
        nova=str.replace(nova,';',' ')
    if '.' in nova:
        nova=str.replace(nova,'.',' ')
    return nova