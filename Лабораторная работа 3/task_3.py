def count_letters(text: str) -> dict:
    text = text.lower()
    bukv_count = {}
    for symbol in text:
        if symbol.isalpha():
            if symbol in bukv_count:
                bukv_count[symbol] += 1
            else:
                bukv_count[symbol] = 0
    return bukv_count


def calculate_frequency(bukv_dict: dict, bukv_count: int) -> dict:
    bukv_freq = {}
    for bukva in bukv_dict:
        bukv_freq[bukva] = bukv_dict[bukva] / bukv_count
    return bukv_freq


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

bukv_dict = count_letters(main_str)

count_bukv = 0
for bukv in bukv_dict:
    count_bukv += bukv_dict[bukv]

res_dict = calculate_frequency(bukv_dict, count_bukv)

for bukva in res_dict:
    print(f"{bukva}: {res_dict[bukva]:.2f}")
