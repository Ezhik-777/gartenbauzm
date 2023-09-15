#!/bin/bash

# Путь к целевой папке
target_directory="fulls/"

# Имя текстового файла для записей
output_file="записи.txt"

# Перейти в целевую папку
cd "$target_directory" || exit 1

# Очистить или создать текстовый файл
> "$output_file"

# Цикл для просмотра файлов и создания записей
for file in *; do
  if [ -f "$file" ]; then
    # Получить имя файла без расширения
    filename_noext="${file%.*}"
    
    # Создать запись в желаемом формате и добавить ее в текстовый файл
    echo "  - image: \"images/gallery/fulls/$file\"" >> "$output_file"
    echo "    thumb: \"images/gallery/thumbs/$file\"" >> "$output_file"
    echo "    button: \"Vergrößern\"" >> "$output_file"
    echo "" >> "$output_file"
  fi
done

echo "Готово! Записи сохранены в файле $output_file."

