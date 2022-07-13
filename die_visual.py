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


print(results)
print(frequencies)