memory_capacity = 1.44 # в мегабайтах
pages_in_book = 100
strings_on_page = 50
chars_in_string = 25
mem_per_char = 4 # в байтах

mem_per_book = pages_in_book * strings_on_page * chars_in_string * mem_per_char # в байтах
mem_per_book /= (1024 ** 2) # в Мб

book_per_discette = int(memory_capacity // mem_per_book)

print("Количество книг, помещающихся на дискету:", book_per_discette)
