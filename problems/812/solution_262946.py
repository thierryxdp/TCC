def retira_pontuacao(frase):
'''Retorna a frase de entrada sem qualquer caracter de pontuação;
	str -> str'''
    frase_nova1=str.replace(frase,'.',' ')
    frase_nova2=str.replace(frase_nova1,',',' ')
    frase_nova3=str.replace(frase_nova2,';',' ')
    frase_nova4=str.replace(frase_nova3,'.',' ')
    frase_nova5=str.replace(frase_nova4,'-',' ')
    frase_nova6=str.replace(frase_nova5,':',' ')
    frase_nova7=str.replace(frase_nova6,'!',' ')
    frase_nova8=str.replace(frase_nova7,'?',' ')
    return frase_nova8