def stockPrice(arr):

    max_profit = -1
    buy_price = 0
    sell_price = 0

    change_buy_index = True

    for i in range(0, len(arr) - 1):

        sell_price = arr[i+1]

        if change_buy_index:
            buy_price = arr[i]

        if sell_price < buy_price:
            change_buy_index = True
            continue
        else:
            temp_profit = sell_price - buy_price

            if temp_profit > max_profit:
                max_profit = temp_profit
            change_buy_index = False

    return max_profit

def countStep(N):

    if N == 1:
        return 1
    if N == 2:
        return 2

    return countStep(N-1) + countStep(N-2)

def patterns(str, all):

    if(len(str) == 0):
        return all
    if(str[0] == "1" or str[0] == "0"):
        for i in range(0, len(all)):
            all[i].append(str[0])
    if(str[0] == "?"):
        len_all = len(all)
        for i in range(0, len_all):
            temp = list(all[i])
            all.append(temp)
        for i in range(0, len(all)):
            if i < len(all) / 2:
                all[i].append("0")
            else:
                all[i].append("1")
    return patterns(str[1:], all)

if __name__ == '__main__':
    # Stock maximum profit
    print(stockPrice([12,22,125,1256,22,1,99,102,5000]))
    # Step counting using recursion
    print(countStep(12))
    # String combination consisting only of 0,1 and?
    print(patterns("011?0100", [[]]))


