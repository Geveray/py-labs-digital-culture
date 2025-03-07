def find_common_participants(first_gr: str, second_gr: str, separator: str = "|"):
    first_set = set(first_gr.lower().split(separator))
    second_set = set(second_gr.lower().split(separator))
    common = list(first_set.intersection(second_set))
    common = [common[i][0].upper() + common[i][1:] for i in range(len(common))]
    return common

participants_first_group = "Иванов|петРов|Сидоров"
participants_second_group = "Петров|СидОров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))

