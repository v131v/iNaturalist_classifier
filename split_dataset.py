import os
import random
import shutil


def move_random_files(source_folder, target_folder, ratio=0.2):
    """
    Перемещает случайные файлы из source_folder в target_folder в заданной пропорции.

    :param source_folder: Путь к исходной папке с файлами.
    :param target_folder: Путь к целевой папке для перемещения.
    :param ratio: Доля файлов для перемещения (от 0 до 1).
    """
    # Создаем папку, если она не существует
    os.makedirs(target_folder, exist_ok=True)

    # Получаем список всех файлов в исходной папке
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Определяем количество файлов для перемещения
    num_files_to_move = int(len(files) * ratio)

    # Выбираем случайные файлы
    files_to_move = random.sample(files, num_files_to_move)

    # Перемещаем файлы
    for file_name in files_to_move:
        source_path = os.path.join(source_folder, file_name)
        target_path = os.path.join(target_folder, file_name)
        shutil.move(source_path, target_path)

    print(f"Перемещено {len(files_to_move)} файлов из {source_folder} в {target_folder}.")


# Использование
source_folder = 'dataset'  # Замените на путь к исходной папке
target_folder = 'dataset_train'  # Замените на путь к целевой папке

move_random_files(source_folder, target_folder)
