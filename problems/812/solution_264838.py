def retira_pontuacao(frase):
    '''Função que recebe uma frase e retorna essa mesma frase, porém, substituindo a pontuação por
    espaço. str -> str'''
    nova_frase = str.replace(frase,'...',' ')
    nova_frase2 = str.replace(nova_frase,':',' ')
    nova_frase3 = str.replace(nova_frase2,';',' ')
    nova_frase4 = str.replace(nova_frase3,"'",' ')
    nova_frase5 = str.replace(nova_frase4,'"',' ')
    nova_frase6 = str.replace(nova_frase5,'-',' ')
    nova_frase7 = str.replace(nova_frase6,'!',' ')
    nova_frase8 = str.replace(nova_frase7,'?',' ')
    nova_frase9 = str.replace(nova_frase8,',',' ')
    nova_frase10 = str.replace(nova_frase9,'.',' ')
    nova_frase11 = str.replace(nova_frase10,'(',' ')
    nova_frase12 = str.replace(nova_frase11,')',' ')
    return nova_frase12