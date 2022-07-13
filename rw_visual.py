import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Continua criando novos passeis enqunto o program estiver ativo
while True:
    #Cria um passeio aleatorio e plota os pontos
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Define tamanho da janela de plotagem
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #Enfatiza o primeiro e o ultimo ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    #Remove eixos
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_runnning = input("Make another? (y/n): ")
    if keep_runnning == 'n': break
