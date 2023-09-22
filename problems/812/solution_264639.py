import string 
def retira_pontuacao(texto):
    n_t = texto.replace(';',' ')
    n_t1= n_t.replace(',',' ')
    n_t2 = n_t1.replace('-',' ')
    n_t3 = n_t2.replace(':',' ')
    n_t4 = n_t3.replace('.',' ')
    n_t5 = n_t4.replace('!',' ')
    return n_t5