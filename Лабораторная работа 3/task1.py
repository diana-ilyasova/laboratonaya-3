def find_fruits_index(items_list, fruits):
    for index, item in enumerate(items_list):
        if item == fruits:
            return index
    return None  # Если товар не найден, возвращает None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_fruits_index(items_list, find_item) # TODO Вызовите функцию, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
