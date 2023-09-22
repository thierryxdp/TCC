def retira_pontuacao(fra):
    fra= fra.replace('?',' ')
    fra= fra.replace('!',' ')
    fra= str.replace(fra,'...','1')
    fra= str.replace(fra,'1',' ')
    fra= fra.replace('.',' ')
    fra= fra.replace(',',' ')
    fra= str.replace(fra,'-',' ')
    return fra