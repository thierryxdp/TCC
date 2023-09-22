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
    lis= retira_pontuacao(fra).strip().lower().split().reverse()
    nfr= retira_pontuacao(fra).strip().lower()
    return lis