def filtra_pares(tuplaV):
    tuplaN=()
    if tuplaV[0]%2==0:
        tuplaN= tuplaN()+ (tuplaV[0],)
    if tuplaV[1]%2==0:
        tuplaN= tuplaN()+ (tuplaV[1],)
    if tuplaV[2]%2==0:
        tuplaN= tuplaN()+ (tuplaV[2],)
    if tuplaV[3]%2==0:
        tuplaN= tuplaN()+ (tuplaV[3],)
        return tuplaN