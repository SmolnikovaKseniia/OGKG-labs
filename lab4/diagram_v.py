import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.cluster import DBSCAN

# Функція для зчитування координат з файлу
def read_coordinates(filename):
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            coordinates.append((x, y))
    return coordinates

# Функція для збереження файлу у вибраному форматі
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
            output_file = f"lab4/output.{format_extension}"
            plt.savefig(output_file, format=format_extension)
            print(f"Файл збережено як {output_file}.")
            break  # Вихід з циклу після успішного збереження
        else:
            print("Неправильний вибір формату! Спробуйте ще раз.")

# Завантаження датасету з файлу
def load_dataset(file_path):
    data = np.array(read_coordinates(file_path))
    return data

# Кластеризація за допомогою DBSCAN
def find_clusters(data, eps=5, min_samples=5):
    db = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = db.fit_predict(data)
    return clusters

# Обчислення центрів ваги для кожного кластеру
def calculate_centroids(data, clusters):
    centroids = []
    unique_clusters = np.unique(clusters)
    for cluster in unique_clusters:
        if cluster != -1:  # Пропускаємо шуми
            cluster_points = data[clusters == cluster]
            centroid = np.mean(cluster_points, axis=0)
            centroids.append(centroid)
    return np.array(centroids)

# Побудова діаграми Вороного для центрів ваги
def voronoi_diagram(centroids, canvas_size=(960, 540)):
    vor = Voronoi(centroids)

    fig, ax = plt.subplots(figsize=(canvas_size[0] / 100, canvas_size[1] / 100), dpi=100)

    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_width=1, line_colors='purple', zorder=1)

    return fig, ax

# Відображення результатів: точок, центрів ваги та діаграми Вороного
def plot_results(data, centroids, canvas_size=(960, 540)):
    fig, ax = voronoi_diagram(centroids, canvas_size)

    ax.scatter(centroids[:, 0], centroids[:, 1], color='blue', s=20, zorder=2)
    ax.scatter(data[:, 0], data[:, 1], color='black', alpha=0.1, s=2, zorder=0)

    ax.set_xlim([0, canvas_size[0]])
    ax.set_ylim([0, canvas_size[1]])
    ax.set_aspect('equal')
    ax.axis('off')

    return fig


file_path = "lab4\DS4.txt"
data = load_dataset(file_path)

clusters = find_clusters(data)
centroids = calculate_centroids(data, clusters)  
fig = plot_results(data, centroids)  
save_file() 
plt.show()  