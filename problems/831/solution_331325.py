def lingua_p(palavra):
    resposta = palavra.lower()
    resposta_real = ""
    for i in range(len(palavra)):
        if resposta[i] in "aeiouáéàóãâú":
           resposta_real += resposta[i] + "p" + resposta[i]
        else:
           resposta_real += resposta[i]      
    return resposta_real