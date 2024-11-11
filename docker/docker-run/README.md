# docker-run

Задания в данном модуле будут проверяться ментором в конце модуля.

Для сдачи данного модуля создайте репозиторий в ([ССЫЛКА GITHUB CLASSROOM]).

### Полезное

- [Установка Docker](https://docs.docker.com/get-docker/)

### Задание

1. Установить Docker, если еще не установлен на вашем компьютере.
2. Запустить контейнер на порту `8888` из официального образа `nginx`:

```bash
docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
```

3. Вывести список активных контейнеров:

```bash
docker ps
```

4. Проверьте запрос на `http://localhost:8888` с помощью `curl`. Должно появиться приветственное сообщение от `nginx`.
5. Остановить запущенный контейнер:

```bash
docker stop jsn-dkr-run
```

6. Вывести список активных контейнеров, чтобы убедиться что нашего контейнера нет в списке.
7. Проверьте запрос `http://localhost:8888` с помощью `curl`. Должна появиться ошибка, так как наш контейнер был остановлен.
8. Вывести список всех контейнеров. В нем должен появиться наш остановленный контейнер.

```bash
docker ps -a
```

9. Все выполенные команды `docker` записать в репозиторий в файл `docker-run/solution.sh`. В скрипте не должно быть команд `curl`.
   Запушить в гит.

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-run.sh

---

### Ответ

root@aman:/home/amangeldi/Desktop/TechOrda/docker/docker-run# docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
Unable to find image 'nginx:mainline' locally
mainline: Pulling from library/nginx
Digest: sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb
Status: Downloaded newer image for nginx:mainline
ab255545695ef6b3ad5818cb703f2ccbf023139c99da32776f674bbabcb62dd2
root@aman:/home/amangeldi/Desktop/TechOrda/docker/docker-run# docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                   NAMES
ab255545695e   nginx:mainline   "/docker-entrypoint.…"   7 seconds ago   Up 6 seconds   0.0.0.0:8888->80/tcp, :::8888->80/tcp   jsn-dkr-run
root@aman:/home/amangeldi/Desktop/TechOrda/docker/docker-run# docker stop jsn-dkr-run
jsn-dkr-run
root@aman:/home/amangeldi/Desktop/TechOrda/docker/docker-run# docker ps -a
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS                      PORTS     NAMES
ab255545695e   nginx:mainline   "/docker-entrypoint.…"   53 seconds ago   Exited (0) 12 seconds ago             jsn-dkr-run

bash ./tester-docker-run.sh 
✅
✅
✅