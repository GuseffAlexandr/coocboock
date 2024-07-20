

def read_ingridient(item: str):
    items = item.split(' | ')
    return {
        'ingredient_name': items[0],
        'quantity': int(items[1]),
        'measure': items[2]
    }


def read_cooc_book(filename: str):
    cooc_book = {}
    with open(filename, 'r') as fout:
        while True:
            name = fout.readline().strip('\n')
            if name == '':
                break
            count = int(fout.readline())
            cooc_book[name] = []
            for _ in range(count):
                ingr = fout.readline().strip('\n')
                cooc_book[name].append(read_ingridient(ingr))
            fout.readline()
    return cooc_book


if __name__ == '__main__':
    cooc_book = read_cooc_book('recipes.txt')
    print(cooc_book)


