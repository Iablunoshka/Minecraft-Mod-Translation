
# Автоматический перевод Minecraft модов на русский язык

Скрипт работает, перебирая предоставленный каталог в поисках файлов en_us.json в файлах модов .jar. Найдя, он считывает английский текст из JSON, переводит его на русский с помощью пакета deep_translator, а затем записывает переведенный текст обратно в новый файл ru_ru.json в файле мода .jar.

## Использование

Для использования скрипта выполните следующие шаги:

1. Убедитесь, что у вас установлен Python 3.
2. Установите необходимые зависимости
3. Запустите скрипт с указанием пути к каталогу с модами для перевода:

   ```bash
   python main.py -i ПУТЬ_К_КАТАЛОГУ_С_МОДАМИ
   ```

4. Скрипт автоматически переведет текст модов и создаст файлы на русском языке.

## Особенности

- Скрипт робатет на большинства версияx *Minecraft*
- Скрипт сам определяет есть ли у мода руская локализацыя если да то он пропускает его
- Если у мода нет  en_us.json он не сможет перевести мод и пропустит его

## Зависимости

Для запуска скрипта вам понадобятся следующие библиотеки:

- `deep_translator`
- `argparse`
- `zipfile`
- `json`

## Важно
- Этот скрипт использует Google Translator, и у него могут быть ограничения или ограничения по скорости перевода. Помните об этих ограничениях при переводе большого количества модов.

- Некоторые моды могут не иметь файлов «en_us.json», или перевод может быть несовершенным из-за автоматического перевода.

- Прежде чем запускать этот скрипт, убедитесь, что у вас есть резервные копии ваших модов, поскольку он изменяет моды, добавляя переведенные файлы.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности можно найти в файле [LICENSE](LICENSE).

## Автор

Автор: @Iablunoshka

## Связь

Если у вас есть вопросы или предложения, вы можете связаться со мной в Discord: 6masia9
