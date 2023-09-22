def filtraMultiplos(num):
    prime = True
    for counter in range(2, int(m.sqrt(num) + 1)):
        if num % counter == 0: 
            prime = False
            print("Entrou e Saiu?")
            break
    return "O numero é primo?", prime