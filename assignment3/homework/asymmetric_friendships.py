import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])

def reducer(key, list_of_values):
    d = {}
    for value in list_of_values:
        if value not in d:
            d[value] = 1
        else:
            d.pop(value)

    for value in d.keys():
        mr.emit((key, value))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
