import csv
import os
import requests
from concurrent.futures import ThreadPoolExecutor


def download_image(row, target_folder):
    image_url = row['image_url']
    file_id = row['id']  # Берем id из CSV
    if image_url:  # Проверяем, что URL не пустой
        try:
            # Полный путь к файлу
            filename = f"{file_id}.jpg"
            filepath = os.path.join(target_folder, filename)

            # Скачиваем изображение
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Скачано: {filename}")
            else:
                print(f"Ошибка загрузки {image_url}: {response.status_code}")
        except Exception as e:
            print(f"Ошибка при обработке {image_url}: {e}")


def download_images(csv_file, target_folder, max_workers=5):
    # Создаем папку, если она не существует
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Читаем CSV-файл и запускаем загрузку в нескольких потоках
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(lambda row: download_image(row, target_folder), reader)


# Использование
csv_file = 'metafile_yellow.csv'  # Замените на путь к вашему CSV-файлу
target_folder = 'dataset'  # Замените на путь к папке для сохранения изображений

download_images(csv_file, target_folder)
