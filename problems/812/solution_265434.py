def retira_pontuacao(fra):
    """Função que retira todas as pontuações de uma frase 
dada.
"""
    fra = str.replace(fra,'?',' ')
    fra = str.replace(fra,'!',' ')
    fra = str.replace(fra,'...','1')
    fra = str.replace(fra,'1',' ')
    fra = str.replace(fra,'.',' ')
    fra = str.replace(fra,',',' ')
    fra = str.replace(fra,'-',' ')
    return fra