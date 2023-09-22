def conta_frases(frase):
    sem_pts1 = str.replace(str.replace(str.replace(str.replace(frase,'...','/'),'.','/'),'!','/'),'?','/')
    l = sem_pts1.split('/')
    return len(l)