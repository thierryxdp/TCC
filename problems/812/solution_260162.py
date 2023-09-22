def retira_pontuacao (f):
    """retirar todas as pontuações da frase f de entrada e substituir por espaço em branco"""
    f=f.replace('!',' ')
    f=f.replace('?',' ')
    f=f.replace('.',' ')
    f=f.replace(';',' ')
    f=f.replace(',',' ')
    f=f.replace('-',' ')
    return f