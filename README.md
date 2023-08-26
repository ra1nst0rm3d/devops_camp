# Cloud.ru DevOps Test Task Solution

## Решил: Олег Сазонов

## 1. Ansible Playbook

Был реализован playbook с шифрованием "секретов" с помощью ansible-vault (пароль от vault записан в файле pwd) и переменные были вынесены в отдельный файл. Инвентарь подготовлен для запуска на локальном хосте. Воспроизведение playbook'а осуществляется через запуск скрипта deploy.sh в папке с playbook.
```console
[ra1n@RyzenLaptop playbook]$ ./deploy.sh
```

## 2. Приложение на Python и Docker
Я использовал библиотеку Python http.server, которая идет "из коробки". Это позволило мне собрать приложение в native binary и не таскать за ним образ Debian с Python 3, а сразу использовать чистый Alpine, как базу. Для сборки контейнера был написан multi-stage Dockerfile, который сначала собирает программу с помощью [Nuitka](https://nuitka.net/) в одном контейнере, потом переносит уже готовый бинарь в Alpine. Это позволило мне сжать контейнер с 120+ Мб до 13Мб! Фантастика, я считаю!

### 2.1 Манифест K8s
Я объединил описание всех необходимых сущностей K8s (deployment, ClusterIp service, namespace) в один файл, дабы прописать одну команду и всё было готово. Понимаю, что в большом проекте такой подход будет мешать, но это и не большой проект :)
Первым делом, создаю namespace с именем devops. Далее, в этом namespace создается deployment под названием test-app с 3 репликами и, уже после всего этого, к ним привязывается ClusterIp service, который просто открывает 8000 порт.
P.S. Я тут засомневался в неоходимости указания $AUTHOR в манифесте, но искренне надеюсь, что я сделал правильно, указав его.
### 2.2 Helm chart
Чарт был просто создан с помощью команды:
```console
[ra1n@RyzenLaptop helm]$ helm create test
```
и подогнан к предыдущему манифесту, ничего сверхъестественного :)