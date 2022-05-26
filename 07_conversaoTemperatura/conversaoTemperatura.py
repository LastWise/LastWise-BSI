def celsiusParaFarenheit(c):

    f = c * 1.8 + 32
    return f

assert(celsiusParaFarenheit(0) == 32)
assert(celsiusParaFarenheit(100) == 212)

def farenheitParaCelsius(f):
    c = (f - 32) / 1.8
    return c

assert(farenheitParaCelsius(32) == 0)
assert(farenheitParaCelsius(212) == 100)