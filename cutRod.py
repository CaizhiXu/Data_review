import time

price = {1:1, 2:3, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:26, 10:30}
length = 12
way_cut = {}
max_values = {}

def cutRod(price, way_cut, max_values, n):
    if n<=0:
        max_values[0] = 0
        way_cut[0] = 0
        return 0

    max_val = -1
    for k in price:
        if k <= n:
            if n-k in max_values:
                new_price = price[k] + max_values[n-k]
            else:
                new_price = price[k] + cutRod(price, way_cut, max_values, n-k)

            if max_val < new_price:
                way_cut[n] = k
                max_val = new_price

    max_values[n] = max_val
    return max_val

def cutRod_print(way_cut, n):
    left_length = n
    i = 1
    while left_length > 0:
        print('Cut {} position = {}'.format(i, way_cut[left_length]))
        i += 1
        left_length = left_length - way_cut[left_length]

start_time = time.time()
print('\nWhen rod length = {}, maximum obtainable value: {}'.format(length, cutRod(price, way_cut, max_values, length)))
print("--- %s seconds ---" % (time.time() - start_time))
print('\nCutting sequence:')
cutRod_print(way_cut, length)