from src.hh import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def search(search_query):
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_api.load_vacancies(search_query)
    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)
    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)
        json_saver.commit("vacancies")
    # json_saver.delete_vacancy(vacancy)
    return vacancies_list


def filter_vacancies(vacancies_list, filter_words):
    if filter_words:
        filter_words = [x.lower() for x in filter_words]
        filtered_vacancies = []
        for vacancy in vacancies_list:
            if vacancy.name.lower() in filter_words:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies
    return vacancies_list


def get_vacancies_by_salary(filtered_vacancies, min_range):
    ranged_vacancies = []
    for vacancy in filtered_vacancies:
        if vacancy.salary_to:
            if int(vacancy.salary_to) >= min_range:
                ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    return sorted(ranged_vacancies, key=lambda vacancy: vacancy.salary_to, reverse=True)


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies):
    for vacancy in top_vacancies:
        print(repr(vacancy))


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    vacancies_list = search(search_query)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    min_range = int(input("Введите минимальную зарплату: "))  # Пример: 100000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, min_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
