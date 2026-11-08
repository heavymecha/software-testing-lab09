# Лабораторная работа 9

Публичный репозиторий: <https://github.com/heavymecha/software-testing-lab09>.

Локальная проверка: `pip install -r requirements.txt`, затем `pytest -v tests`.
Workflow `.github/workflows/run-tests.yml` автоматически выполняет те же тесты
при `push` и `pull_request` на Ubuntu 24.04 и Python 3.12. В CI сохраняется
JUnit XML-файл `results.xml` в рабочей директории запуска.
