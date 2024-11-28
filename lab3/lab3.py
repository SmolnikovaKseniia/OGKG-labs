import matplotlib.pyplot as plt
import numpy as np

def read_coordinates(filename):
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            coordinates.append((x, y))
    return coordinates

def save_file():
    print("Оберіть формат файлу для збереження:")
    print("1) PNG")
    print("2) JPG")
    print("3) PDF")
    print("4) SVG")
   
    file_formats = {1: "png", 2: "jpg", 3: "pdf", 4: "svg"}
   
    while True:
        choice = input("Введіть число (1-4): ")
        if choice.isdigit() and int(choice) in file_formats:
            format_extension = file_formats[int(choice)]
            output_file = f"output.{format_extension}"
            plt.savefig(output_file, format=format_extension)
            print(f"Файл збережено як {output_file}.")
            break
        else:
            print("Неправильний вибір формату! Спробуйте ще раз.")

def convex_hull(points):

    points = sorted(set(points))

    if len(points) <= 1:
        return points

    # Перетин векторів для визначення напрямку повороту
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Нижня оболонка
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Верхня оболонка
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Повертаємо точки опуклої оболонки
    return lower[:-1] + upper[:-1]


def main():

    input_file = 'DS4.txt'
    convex_hull_file = 'convex_hull.txt'  # Файл для збереження опуклої оболонки

    # Зчитування координат
    points = read_coordinates(input_file)

    # Знаходження опуклої оболонки
    hull_points = convex_hull(points)

    # Збереження опуклої оболонки у файл
    with open(convex_hull_file, 'w') as file:
        for x, y in hull_points:
            file.write(f"{x} {y}\n")
    print(f"Опукла оболонка збережена у файл: {convex_hull_file}")

    # Підготовка до візуалізації
    points = np.array(points)
    hull_points = np.array(hull_points)

    # Встановлення розмірів полотна
    canvas_width = 960
    canvas_height = 540

    # Побудова графіка
    plt.figure(figsize=(canvas_width / 100, canvas_height / 100), dpi=100)
    plt.gca().axis('off')

    # Відображення точок вихідного датасету
    plt.scatter(points[:, 0], points[:, 1], c='purple', s=10)

    # Відображення опуклої оболонки
    hull_closed = np.vstack([hull_points, hull_points[0]])
    plt.plot(hull_closed[:, 0], hull_closed[:, 1])

    save_file()

if __name__ == "__main__":
    main()
