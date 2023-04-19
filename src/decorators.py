def berechne_dreimal(func):
    def wrapper_do_tripple(x):
        func(x)
        func(x)
        func(x)
        return x
    return wrapper_do_tripple


