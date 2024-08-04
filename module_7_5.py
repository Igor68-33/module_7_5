# Файлы в операционной системе
import os
import time

directory = "."
print(os.getcwd())
corr_dir = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        # filepath = os.path.abspath(file)  # можно использовать абсолютный путь к файлу в текущей папке
        filepath = os.path.join(corr_dir, root[2:], file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(filepath).st_size
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
