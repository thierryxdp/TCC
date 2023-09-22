def retira_pontuacao(frase):
    """Dada uma frase a função retira toda pontuação
    	str-->str"""
    frase1=(str.replace(frase,',','')).replace('.','')
    return (frase1)