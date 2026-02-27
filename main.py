from worker import WORKER


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Введите корректное положительное число.")


def main():
    n = read_positive_int("Сколько работников ввести? ")
    workers = []

    for i in range(n):
        print(f"\nРаботник #{i + 1}")
        worker = WORKER.from_input()
        workers.append(worker)

    threshold = read_positive_int("\nВведите минимальный стаж (в годах): ")

    result = [w for w in workers if w.is_experience_gt(threshold)]

    print("\nРезультат:")
    if not result:
        print("Работников со стажем больше указанного значения нет.")
    else:
        print("Работники со стажем больше указанного значения:")
        for w in result:
            print(w.get_short_name())


if __name__ == "__main__":
    main()