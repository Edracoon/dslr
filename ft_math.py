import math

def ft_percentile(tab, percent):
    tab.sort()
    index = round((percent / 100) * (len(tab) - 1))
    return tab[index]

def ft_mean(tab):
    total = 0
    for row in tab:
        total += row
    return total / len(tab)

def ft_standard_deviation(tab):
    mean = ft_mean(tab)
    sum = 0
    for row in range(len(tab)):
        sum += (tab[row] - mean) ** 2
    return math.sqrt(sum / len(tab))
