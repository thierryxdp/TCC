def conta_frases(frase):
    q_pts = len(frase.split('.'))-1
    q_int = len(frase.split('!'))-1
    q_qst = len(frase.split('?'))-1
    q_ppp = len(frase.split('...'))-1
    return q_pts+q_int+q_qst-2*q_ppp