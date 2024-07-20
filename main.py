

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


def get_shop_list_by_dishes(cooc_book, dishes, person_count):
    count_food = {}
    for dish in dishes:
        recipie = cooc_book[dish]
        for item in recipie:
            name = item['ingredient_name']
            count = item['quantity']
            measure = item['measure']
            if name in count_food:
                count_food[name]['quantity'] += person_count * count
            else:
                count_food[name] = {
                    'quantity': person_count * count,
                    'measure': measure,
                }
    return count_food


if __name__ == '__main__':
    cooc_book = read_cooc_book('recipes.txt')
    print(cooc_book)

    print(get_shop_list_by_dishes(cooc_book, ['Омлет', 'Омлет', 'Запеченный картофель'], 3))


