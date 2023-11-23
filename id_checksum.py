def id_checksum(id_card_17):
    if len(id_card_17) < 17:
        raise ValueError()

    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

    checksum_mapping = {
        0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'
    }

    checksum = 0

    for i in range(17):
        checksum += int(id_card_17[i]) * factors[i]

    checksum %= 11

    return checksum_mapping[checksum]

if __name__ == '__main__':
    id_card_17 = input()
    id_card_17 = id_card_17.strip()
    try:
        checksum = id_checksum(id_card_17)
        print(checksum)
    except ValueError:
        print('error')
