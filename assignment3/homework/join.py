import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    #mr.emit((key, list(set(list_of_values))))
    orders = []
    lineitems = []
    for record in list_of_values:
        if record[0] == 'order':
            orders.append(record)
        else:
            lineitems.append(record)

    for order in orders:
        for lineitem in lineitems:
            mr.emit(order + lineitem)

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
