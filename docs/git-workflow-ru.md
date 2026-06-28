# Как загружать и обновлять репозиторий

Репозиторий: https://github.com/KuznetsovKarazin/fundamentals-of-iot-notebooks

## Первый запуск

Если репозиторий уже создан на GitHub:

```bash
git clone https://github.com/KuznetsovKarazin/fundamentals-of-iot-notebooks.git
cd fundamentals-of-iot-notebooks
```

Скопируйте содержимое этого стартового пакета в папку репозитория, затем выполните:

```bash
git add .
git commit -m "Initial companion notebooks structure"
git push origin main
```

Если GitHub попросит авторизацию, используйте GitHub Desktop или Personal Access Token вместо обычного пароля.

## Добавление новой главы

1. Сохраните новый ноутбук в папку `notebooks/`.
2. Назовите его по шаблону:

```text
chXX-short-topic-practice.ipynb
```

Например:

```text
ch11-advanced-sensor-technologies-practice.ipynb
```

3. Проверьте, что ноутбук запускается полностью:

```bash
jupyter nbconvert --to notebook --execute notebooks/ch11-advanced-sensor-technologies-practice.ipynb --output /tmp/check.ipynb
```

На Windows можно проще открыть ноутбук в Colab или Jupyter и выполнить **Run all**.

4. Обновите таблицы в двух файлах:

```text
README.md
docs/notebook-index.md
```

5. Сделайте commit и push:

```bash
git add notebooks/ README.md docs/notebook-index.md
git commit -m "Add Chapter 11 practical notebook"
git push origin main
```

## Обновление существующего ноутбука

Если вы исправили уже загруженный ноутбук:

```bash
git status
git add notebooks/ch10-common-iot-sensors-practice.ipynb
git commit -m "Update Chapter 10 notebook"
git push origin main
```

## Важное правило для ссылок и QR-кодов

Пока репозиторий приватный, ссылки могут быть недоступны читателям. Перед вставкой окончательных QR-кодов в учебник:

1. Проверьте имя репозитория.
2. Проверьте имена файлов.
3. Сделайте репозиторий публичным.
4. Создайте release/tag, например `v1.0`.
5. Используйте стабильную страницу репозитория или ссылку на release.

Не переименовывайте репозиторий и файлы после публикации ссылок в учебнике.
