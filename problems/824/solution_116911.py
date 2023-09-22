def uppCons(frase):
    """Função que recebe uma frase e retorna essa frase com todas as suas consoantes em maiúsculo;
    str - str"""
i = 0
	while i < len(frase):
        if frase[i] not in 'aâãáàeêéèiûííoôõóòuûúùAÂÃÁÀEÊÉÈIÎÍÌOÒÓÕUÙÚÛ':
            frase = frase[:i] + str.upper(frase[i]) + frase[i+1:]
        i = i + 1
	return frase