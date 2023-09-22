def melhor_volta(matrixSixXTen):
    '''Function that receives a matrix with six lines,
    representing six diferent drivers, and ten columns,
    representing diferent lap times in seconds for each driver. It
    will be returned a tuple  with the owner of the best 
    lap time, the time itself and the lap that it ocurred.
    List --> Tuple.'''
    lapTimes = []
    for driver in matrixSixXTen:
         lapTimes += driver
    bestLapTime = min(lapTimes)
    index = lapTimes.index(bestLapTime)
    driverNumber = str(index+10)[0]
    lap = index
    while lap > 10:
        lap -= 10
    bestTimeLap = str(lap+1)[0]
    if lap == 9:
        return (int(driverNumber),bestLapTime,10)
    else:
        return (int(driverNumber),bestLapTime,int(bestTimeLap))