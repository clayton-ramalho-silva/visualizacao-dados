import pygal
from die import Die

#crie um D6
die = Die()

#faz alguns lançamentos e armazena os resultados em lista
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analisa os resultados

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


#visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)