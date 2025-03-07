def find_items(products: list, item: str):
    item = item.lower()
    for i in range(len(products)):
        products[i] = products[i].lower()
    try:
        return products.index(item)
    except:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'Груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_items(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
