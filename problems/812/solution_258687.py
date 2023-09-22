def retira_pontuacao(frase):
    '''funcao que recebe uma frase e retorna ela onde todos os caracteres de pontuaçao vao ser substituídos por espaco; int-->int'''
    x=str.replace(frase,'.',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,':',' ')
    u=str.replace(z,'-',' ')
    s=str.replace(u,';',' ')
    p=str.replace(s,'!',' ')
    q=str.replace(p,'?',' ')
    return q