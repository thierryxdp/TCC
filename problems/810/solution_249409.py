def retira_pontuacao(texto):
    n_t = texto.replace(';',' ')
    n_t1= n_t.replace(',',' ')
    n_t2 = n_t1.replace('-',' ')
    n_t3 = n_t2.replace(':',' ')
    n_t4 = n_t3.replace('.',' ')
    n_t5 = n_t4.replace('!',' ')
    n_t6 = n_t5.replace('?',' ')
    return n_t6
def inverte(texto):
    """Põe frase de traz para a frente ; str ==>str"""
    nova_frase = retira_pontuacao(texto)
    nov= nova_frase.split()
    print (nov)
    ac= nov[::-1]
    act=  ' '.join(ac)
    return act