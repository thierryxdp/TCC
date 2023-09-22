def retira_pontuacao(fra):
    fra= fra.replace('?',' ')
    fra= fra.replace('!',' ')
    fra= str.replace('...','1')
    fra= str.replace('1',' ')
    fra= fra.replace('.',' ')
    return fra