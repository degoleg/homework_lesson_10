import json


def load_candidates():
    """
    Функция грузит данные из файла
    :return:
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)



def get_all():
    """
    Функция покажет всех кандидатов
    :return:
    """
    return load_candidates()


def get_by_pk(pk):
    """
    Функция вернет кандидата по pk
    :param pk:
    :return:
    """
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skill_name):
    """
    Функция вернет кандидатов по навыку
    :param skill_name:
    :return:
    """
    return


def get_candidate_by_skill(skill):
    """
    Функция перебирает навык в списке наыков кандидата
    :param skill_name:
    :return:
    """
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates



