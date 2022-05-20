import math

INT_MAX = float(4 ** 18)
INT_MIN = float(-1 * (4 ** 18))

def ft_percentile(tab, percent):
    tab.sort()
    index = round((percent / 100) * (len(tab) - 1))
    return tab[index]

def ft_mean(tab): # Moyenne
    total = 0
    for row in tab:
        total += row
    return total / len(tab)

def ft_standard_deviation(tab): # Ecart type
    mean = ft_mean(tab)
    sum = 0
    for row in range(len(tab)):
        sum += (tab[row] - mean) ** 2
    return math.sqrt(sum / len(tab))

def ft_normalize(tab, minmax): # data [minx miny maxx maxY]
    normalized = []
    for i in range(len(tab)):
        x = (tab[i] - minmax[0]) / (minmax[1] - minmax[0])
        normalized.append(x)
    return normalized

def ft_minmax(data):
    min = INT_MAX
    max = INT_MIN
    for i in range(len(data)):
        if data[i] < min:
            min = data[i]
        if data[i] > max:
            max = data[i]
    return min, max