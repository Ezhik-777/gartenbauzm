from PIL import Image

# Путь к исходным фотографиям
source_path = "fulls/"
# Путь для сохранения миниатюр
output_path = "thumbs/"

# Размер миниатюры (в пикселях)
thumbnail_size = (450, 450)  # Замените этот размер на желаемый размер

# Получаем список файлов в исходной директории
import os
image_files = [f for f in os.listdir(source_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

# Создаем миниатюры для каждой фотографии
for image_file in image_files:
    try:
        # Открываем исходную фотографию
        img = Image.open(os.path.join(source_path, image_file))
        
        # Обрезаем изображение до квадратной формы
        width, height = img.size
        size = min(width, height)
        left = (width - size) / 2
        top = (height - size) / 2
        right = (width + size) / 2
        bottom = (height + size) / 2
        img = img.crop((left, top, right, bottom))
        
        # Создаем миниатюру с указанным размером и заполняем всю миниатюру
        img.thumbnail(thumbnail_size, Image.LANCZOS)  # Используем фильтр LANCZOS для сглаживания
        
        # Создаем новое имя для миниатюры (например, добавляем '_thumb' к исходному имени)
        thumbnail_name = os.path.splitext(image_file)[0] + '_thumb' + os.path.splitext(image_file)[1]
        
        # Сохраняем миниатюру
        img.save(os.path.join(output_path, thumbnail_name))
        
        print(f"Создана миниатюра для {image_file}")
    
    except Exception as e:
        print(f"Ошибка при обработке {image_file}: {str(e)}")
