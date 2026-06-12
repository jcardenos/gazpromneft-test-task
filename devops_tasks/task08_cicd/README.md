# Task 8

## Суть задания

Развёрнут Jenkins, в нём сконфигурировано 3 джобы:
- Job_1 делает клонирование репозитория
- Job_2 удаляет файл ```code3.txt```
- Job_3 коммитит и пушит изменения в репозиторий на github.

## Ход выполнения задания

1. Запустим контейнер Jenkins.

![](screenshots/1.%20jenkins%20run.png)

2. Получим пароль администратора.

![](screenshots/2.%20get%20pass.png)

3. Введём пароль на IP_машины:8080.

![](screenshots/3.%20enter%20pass.png)

4. Выберем Install suggested plugins

![](screenshots/4.%20install%20suggested%20plugins.png)

5. Jenkins установлен

![](screenshots/5.%20jenkins%20installed.png)

6. Создадим тестовый репозиторий, в который положим несколько файлов.

![](screenshots/6.%20gitrepo.png)

7. Настроим Github Token, для этого зайдём в Settings - Developer Settings - Personal access tokens 

![](screenshots/7.%20token.png)

8. Создаём Job 1.

![](screenshots/8.%20Job_1%20create.png)

9. Конфигурируем на выполнение раз в минуту

![](screenshots/9.%20Job_1%20configure1.png)

10. Создаем build step на выполнение shell кода

![](screenshots/10.%20Job_1%20configure%202.png)

11. Пишем скрипт для клонирования репо

```bash
rm -rf /var/jenkins_home/shared-repo

echo "Клонирование репозитория"

git clone https://github.com/jcardenos/task08_jenkins_test \
    /var/jenkins_home/shared-repo

echo "Репозиторий очищен"

ls -la /var/jenkins_home/shared-repo
```

Вставляем скрипт внутрь созданного ```build step```:

![](screenshots/11.%20Job_1%20configure%203.png)

12. Сохраняем Job_1, но держим в голове, что нам предстоит его отредактировать и добавить ```post-build action```, который будет автоматически дёргать ```Job_2```. Поэтому сначала создадим ```Job_2``` и ```Job_3```, а затем добавим ```post-build actuion``` для обеих джоб.

Создадим ```Job_2``` с выполнением такого shell-code при билде:

```bash
cd /var/jenkins_home/shared-repo

echo "Файлы до удаления:"

ls -la

rm -f code3.txt

echo "Файл удален, Job_2 отработала"

ls -la

git status
```

![](screenshots/12.%20Job_2%20configure.png)

Создадим ```Job_3``` с выполнением такого shell кода:

```bash
cd /var/jenkins_home/shared-repo

git config user.name "jenkins"
git config user.email "jenkins@jenkins.com"

git add .

git commit -m "Файл удален Джобой 2, Job_3 пушит изменённый репозиторий." || echo "Нечего коммитить"

git push https://my_token@github.com/jcardenos/task08_jenkins_test.git HEAD:master
```

где ```my_token``` - это ```Access Token```, который генерировался на ```шаге 7```.

![](screenshots/13.%20Job_3%20configure1.png)

13. Добавим ```post-build actions``` для ```Job_1``` (вызов ```Job_2```) и для ```Job_2``` (вызов ```Job_3```).

![](screenshots/14.%20Job1%20after%20build.png)

![](screenshots/15.%20Job2_after%20build.png)

14. Проверяем, что джоба отработала.

![](screenshots/16.%20Result.png)

15. Для тестирования поменяем во второй джобе скрипт, удалим теперь файл code2.txt, убедимся что джобы проходят.

![](screenshots/17.%20test%20code2.png)

![](screenshots/18.%20test%20code2%202.png)

![](screenshots/19.%20jenkins%20jobs.png)

Ссылка на тестовый репозиторий, с которым выполнялись манипуляции: https://github.com/jcardenos/task08_jenkins_test