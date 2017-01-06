
# syntactic sugar for using function closures

def query(function):
    return lambda value: __closure(function, value)


def __closure(function, value):
    return lambda element: function(element, value)
