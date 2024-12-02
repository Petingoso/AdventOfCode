# Parte 1
input = open('./02.input', 'r')
# input = [
# "7 6 4 2 1",
# "1 2 7 8 9",
# "9 7 6 2 1",
# "1 3 2 4 5",
# "8 6 4 4 1",
# "1 3 6 7 9"]
#
safe_sum = 0

for line in input:
    lista = [int(x) for x in line.split()]
    deltas_lista = []

    for i in range(len(lista)-1):
        deltas_lista.append(lista[i+1]-lista[i])

    n_inc = 0
    n_dec = 0
    fail = False

    for i in deltas_lista:
        if i == 0 or abs(i)>3:
            fail = True
            break

        if i>0:
            n_inc+=1

        elif i<0:
            n_dec+=1 

    if not((n_dec == 0 and n_inc != 0) or (n_inc == 0 and n_dec != 0)):
        fail = True

    if not fail:
        safe_sum+=1

print(safe_sum)

##  Parte 2
# input = [
# "7 6 4 2 1",
# "1 2 7 8 9",
# "9 7 6 2 1",
# "1 3 2 4 5",
# "8 6 4 4 1",
# "1 3 6 7 9"]

input.seek(0)

def is_safe(deltas):
    n_inc = 0
    n_dec = 0
    n_failures = 0

    for i in deltas:
        if i == 0 or abs(i) > 3:
                return False

        if i > 0:
            n_inc += 1
        elif i < 0:
            n_dec += 1

    return (n_dec < 1 and n_inc != 0) or (n_inc < 1 and n_dec != 0)

safe_sum = 0

for line in input:
    lista = [int(x) for x in line.split()]
    deltas_lista = []

    for i in range(len(lista)-1):
        deltas_lista.append(lista[i+1]-lista[i])

    if is_safe(deltas_lista):
        safe_sum+=1
    else:
        for j in range(len(deltas_lista)+1):
            # remove one from list each iteration
            lista_copy = lista[:j] + lista[j+1:]
            deltas_lista = []
            # recalculate deltas
            for i in range(len(lista_copy)-1):
                deltas_lista.append(lista_copy[i+1]-lista_copy[i])

            # check if we remove one makes it safe
            if is_safe(deltas_lista): 
                safe_sum+=1
                break


print(safe_sum)
