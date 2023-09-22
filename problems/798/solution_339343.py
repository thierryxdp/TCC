# Coloque um comentário dizendo o que a função faz
def freq_palavras(frases):
    p = palavra();
    for palavra in frases:
        palavra = palavra.strip()
        palavra = palavra.lower()
        words = palavra.split(" ")
        
        for word in words:
            if frases in palavras:
                p[frases] = p[frases] + 1
                else:
                    p[frases] = 1
                    for key in list(p.keys()):
                        return (key, "":"", p[key])
                
        
    
# Escolha nomes elucidativos para suas variáveis