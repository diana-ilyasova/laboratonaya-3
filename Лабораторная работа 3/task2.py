# TODO Напишите функцию find_common_participants
def find_common_participants (list1, list2, separator=','):
    participants_first_group = set(list1.split(separator))
    participants_second_group = set(list2.split(separator))
    common_participants = participants_first_group.intersection(participants_second_group)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)

print("Общие участники:", common_participants)