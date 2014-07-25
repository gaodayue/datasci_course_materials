import sys
import MapReduce

mr = MapReduce.MapReduce()

dimensions = 5 # input matrix is 5x5

def mapper(record):
    if record[0] == 'a':
        for col in xrange(dimensions):
            mr.emit_intermediate((record[1], col), record)
    else:
        for row in xrange(dimensions):
            mr.emit_intermediate((row, record[2]), record)

def reducer(key, list_of_values):
    d = {}
    for record in list_of_values:
        if record[0] == 'a':
            if record[2] not in d:
                d[record[2]] = [record[3], 0]
            else:
                d[record[2]][0] = record[3]
        else:
            if record[1] not in d:
                d[record[1]] = [0, record[3]]
            else:
                d[record[1]][1] = record[3]
    
    value = sum(x[0] * x[1] for x in d.itervalues())
    print key
    mr.emit((key[0], key[1], value))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
