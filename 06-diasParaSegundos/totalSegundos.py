def totalSegundos(dias, horas, minutos, segundos):
    '''
    Recebe uma data em dias com horas, minutos e segundos, e retorna a data em segundos.

    '''
    totalsegundos = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)
    return totalsegundos

# Testes da função
assert(totalSegundos(0,0,0,0) == 0)
assert(totalSegundos(0,0,0,1) == 1)
assert(totalSegundos(0,0,1,1) == 61)
assert(totalSegundos(0,1,0,1) == 3601)
assert(totalSegundos(0,1,1,1) == 3661)
assert(totalSegundos(1,1,1,1) == 90061)
