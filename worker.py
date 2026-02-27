from datetime import date


class WORKER:
    def __init__(self,
                 surname: str = "",
                 name_initial: str = "",
                 patronymic_initial: str = "",
                 position: str = "",
                 salary: int = 0,
                 year_hired: int = 0):

        self.surname = surname
        self.name_initial = name_initial
        self.patronymic_initial = patronymic_initial
        self.position = position
        self.salary = salary
        self.year_hired = year_hired

    # Дополнительный "конструктор"
    @classmethod
    def from_input(cls):
        surname = input("Фамилия: ").strip()
        name_initial = input("Инициал имени (например, А): ").strip()
        patronymic_initial = input("Инициал отчества (например, А): ").strip()
        position = input("Должность: ").strip()
        salary = int(input("Зарплата: ").strip())
        year_hired = int(input("Год поступления: ").strip())

        return cls(surname,
                   name_initial,
                   patronymic_initial,
                   position,
                   salary,
                   year_hired)
    def experience_years(self, current_year=None):
        if current_year is None:
            current_year = date.today().year
        return max(0, current_year - self.year_hired)

    def is_experience_gt(self, threshold, current_year=None):
        return self.experience_years(current_year) > threshold

    def get_short_name(self):
        return f"{self.surname} {self.name_initial}.{self.patronymic_initial}."

    def display(self):
        print(f"{self.get_short_name()} | {self.position} | "
              f"ЗП: {self.salary} | Год приема: {self.year_hired}")

    def __del__(self):
        pass