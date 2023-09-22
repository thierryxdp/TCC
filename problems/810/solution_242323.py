def retira_pontuacao(frase):
    """Dada uma frase a função retira toda pontuação
    	str-->str"""
    frase1=str.replace(frase,',',' ')
    frase2=str.replace(frase1,'-',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,';',' ')
    frase5=str.replace(frase4,':',' ')
    frase6=str.replace(frase5,'!',' ')
    frase7=str.replace(frase6,'?',' ')
    frase8=str.replace(frase7,'.',' ')
    return frase8

def inverte(frase):
    frase_sem_pontuacao=(retira_pontuacao(frase))
    frase_minuscula=str.lower(frase_sem_pontuacao)
    partes_frase = (str.split(frase_minuscula, ' '))
    frase_inversa = partes_frase[::-1]
    x=str.join(' ',frase_inversa)
    
    return str.strip(x)