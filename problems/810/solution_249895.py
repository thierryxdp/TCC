def retira_pontuacao(fra):
    """Função que retira todas as pontuações de uma frase dada.
"""
    fra= fra.replace('?',' ')
    fra= fra.replace('!',' ')
    fra= str.replace(fra,'...','1')
    fra= str.replace(fra,'1',' ')
    fra= fra.replace('.',' ')
    fra= fra.replace(',',' ')
    fra= str.replace(fra,'-',' ')
    return fra

def inverte(fra):
    lis= retira_pontuacao(fra).lower().split()
    #inv= list.reverse(lis)
    nfr= retira_pontuacao(fra).lower()
    return retira_pontuacao(fra)