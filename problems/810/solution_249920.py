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
    """Função remove pontuação, coloca em letra minúscula e inverte a ordem das palavras
assinatura: str --> str
"""
    nfr= retira_pontuacao(fra).lower().strip()
    lis= nfr.split()
    inv= lis[-1::-1]
    sti= str.join(' ',inv)
    return sti