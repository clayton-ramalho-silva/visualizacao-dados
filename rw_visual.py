import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Continua criando novos passeis enqunto o program estiver ativo
while True:
    #Cria um passeio aleatorio e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_runnning = input("Make another? (y/n): ")
    if keep_runnning == 'n': break
