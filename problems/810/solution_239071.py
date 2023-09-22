def inverte(frase):
    '''Esta função, dada uma frase, retorna uma outra frase
    que contém as mesmas palavras só que na ordem inversa, sem
    letras maiúsculas e sem pontuação.'''
    
    pontuacao_1=str.replace(frase,'/',' ')
    pontuacao_2=str.replace(pontuacao_1,'!',' ')
	pontuacao_3=str.replace(pontuacao_2,'?',' ')
    pontuacao_4=str.replace(pontuacao_3,'-',' ')
    pontuacao_5=str.replace(pontuacao_4,',',' ')
    pontuacao_6=str.replace(pontuacao_5,':',' ')
    pontuacao_7=str.replace(pontuacao_6,';',' ')
    pontuacao_8=str.replace(pontuacao_7,'.',' ')
    
    frase1=str.split(str.lower(pontuacao_8))
    frase_invertida=str.join('frase1',frase1[-1::-1])
    
    return frase_invertida