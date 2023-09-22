import re 
def conta_frases(texto):
    
texto="Preciso tirar um cochilo.Meus Deus!Que horas sao? Vou perder a minha aula..."

pontuacao= re.split('\.|\!|\?|\.\.\.',texto)

print(len(pontuacao))