def lingua_p(palavra):	
    """
    Recebe uma palavra e retorna essa mesma palavra na língua do P,
    onde após cada vogal, insere-se a letra p e repete-se a vogal;
    str -> str
    """
for letra in palavra:
    if letra == 'a':
    	palavra = palavra.replace('a','apa')
    	palavra = palavra.replace('ã','ãpã')
    	palavra = palavra.replace('á','ápá')
    	palavra = palavra.replace('â','âpâ')
    	palavra = palavra.replace('e','epe')
    	palavra = palavra.replace('ê','êpê')
    	palavra = palavra.replace('é','épé')
    	palavra = palavra.replace('i','ipi')
    	palavra = palavra.replace('í','ípí')
    	palavra = palavra.replace('î','îpî')
    	palavra = palavra.replace('o','opo')
    	palavra = palavra.replace('õ','õpõ')
    	palavra = palavra.replace('ó','ópó')
    	palavra = palavra.replace('ô','ôpô')
    	palavra = palavra.replace('u','upu')
    	palavra = palavra.replace('ú','úpú')
    	palavra = palavra.replace('û','ûpû')
return palavra