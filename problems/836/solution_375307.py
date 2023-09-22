def busca(sector, matrix):
    '''Given a sector and a list with lists inside it that contains 
    the information of a worker, including a name, a number of
    registration, a sector and a phone number, as parameters,
    the function returns another list with the workers that work 
    in the sector.
    Str, List --> List.'''
    sectorWorkers = []
    for worker in matrix:
        if worker[2] == sector:
            sectorWorkers += [worker[0],worker[1],worker[3]]
    return sectorWorkers