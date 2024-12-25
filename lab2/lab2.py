import matplotlib.pyplot as plt
import os

def read_coordinates(filename):
    coordinates = []
    if not os.path.exists(filename):
        print(f"Помилка: Файл '{filename}' не знайдено.")
        exit()
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

def main():
    input_file = 'DS4.txt'  
    coordinates = read_coordinates(input_file)

    canvas_width = 960
    canvas_height = 540

    # Побудова графіка
    plt.figure(figsize=(canvas_width / 100, canvas_height / 100), dpi=100)
    plt.gca().axis('off')

    # Відображення точок
    x_coords, y_coords = zip(*coordinates)
    plt.scatter(x_coords, y_coords, c='purple', marker='o')

    save_file()

if __name__ == "__main__":
    main()