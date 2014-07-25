import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    document_id = record[0]
    text = record[1]
    for word in text.split():
        mr.emit_intermediate(word, document_id)

def reducer(key, list_of_values):
    mr.emit((key, list(set(list_of_values))))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
