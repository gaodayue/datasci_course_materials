import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[:-10], None)

def reducer(key, list_of_values):
    mr.emit(key)

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
