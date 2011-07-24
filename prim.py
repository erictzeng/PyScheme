import data

def plus(*args):
    return sum(args)

##### List Procedures ###################
def set_car_bang(cons_pair, new_car):
    cons_pair.car = new_car

def set_cdr_bang(cons_pair, new_cdr):
    cons_pair.cdr = new_cdr

def list(*args):
    if len(args) == 0:
        return NIL()
    else:
        return reduce(lambda accum, next: cons(next, accum), args[::-1], None)

def append_bang(list1, list2):
    lastPair = None
    currPair = list1
    while True:
        if currPair.cdr == NIL:
            lastPair = currPair
        else:
            currPair = currPair.cdr
    lastPair.cdr = list2

def append(list1, list2):
    new_list = copy.deepycopy(list1)
    append_bang(new_list, list2)
    return new_list

def cons(car, cdr):
    return data.ConsPair(car, cdr)

############## Vector procedures ############

def vector_ref(vec, index):
    return vec.vector_ref(index)

def vector_set_bang(vec, index, new_val):
    vec.vector_set_bang(index, new_val)

def vector(*args):
    vec = Vector()
    vec.init_with_vals(*args)
    return vec

def make_vector(*args):
    vec = Vector()
    if len(args) == 1:  # i.e. (make-vector 3)
        vec.init_with_length(args[0])
        return vec
    elif len(args) == 2:  # i.e. (make-vector 3 'hi)
        vec.init_with_initial_val(args[0], args[1])
        return vec
    else:
        raise Exception("incorrect number of arguments")
