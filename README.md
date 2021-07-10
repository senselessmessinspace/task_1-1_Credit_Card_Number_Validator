# Отчёт о тестировании Credit Card Number Validator

## Краткое описание

10.07.2021 было проведено функциональное модульное тестирование приложения Credit Card Number Validator. Проводилось тестирование новой функциональности - позитивные, негативные сценарии.

На тестирование затрачено: 4 часа

### В результате тестирования выявлены следующие дефекты:
* [Номер валидной карты VISA длиной 19 символов не валидируется программой Credit Card Number Validator ](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/1)
* [Номер валидной карты American Express длиной 15 символов не валидируется программой Credit Card Number Validator](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/2)
* [Номер невалидной карты длиной 16 символов валидируется программой Credit Card Number Validator](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/3)
* [Специальные символы длиной 16 символов вызывают ошибку работы программы Credit Card Number Validator](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/4)
* [Номера карт нестандарной длины не валидируются программой Credit Card Number Validator](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/5)

## Описание процесса тестирования

В процессе тестирования использовались следующие артефакты*:
* [чек-лист тестирования](CHECK_LIST.md)
* Набор тестовых данных

### В качестве тестовых данных использовались данные:
* Валидные номера кредитных карт: 
    * [Генератор номеров кредитных карт №1](https://www.freeformatter.com/credit-card-number-generator-validator.html#cardFormats)
    * [Генератор ноперов кредитных карт №2](https://www.vccgenerator.com/)
    * [Генератор ноперов кредитных карт №3](https://cartoved.ru/common/generator-kreditnyh-kart.html)
* Невалидные номера кредитных карт: 16 символов, цифры, верные по алгоритму Луна, но не являются номерами карт (неверный BIN).

    * [Проверка невалидности номера](https://ru-rr.ru/)

Тестовые данные:
* Валидные номера кредитных карт:
```
№1
Номер карты             Ожидаемый результат
---------------------------------------------
VISA (16 и 19 символов):
4539187030321662        "Result is OK"
4318924024036373814     "Result is OK"
---------------------------------------------
MasterCard (16 символов):
2720996388116935        "Result is OK"
---------------------------------------------
American Express(AMEX) (15 символов):
378575763921355         "Result is OK"
---------------------------------------------

№3
Номер карты             Ожидаемый результат
---------------------------------------------
Visa
4345567488457740048    "Result is OK"
---------------------------------------------
MasterCard
5415577376735978        "Result is OK"
---------------------------------------------
```
* Проверенные невалидные номера кредитных карт:
```
Номер карты             Ожидаемый результат
---------------------------------------------
2640647807971791        "Result is FAIL"
7293790973691683        "Result is FAIL"
1111101000000000        "Result is FAIL"
```
* Символы
```
-!@#$%^&*()+\|/?        "Result is FAIL"
```
* Символы и цифры (16 символов)
```
-123456789012345        "Result is FAIL"
```
* Номера длинные и короткие (верные по алгоритму Луна) - пограничные значения
```
            Номер карты             Ожидаемый результат
            ---------------------------------------------
11 символов 93375973364             "Result is FAIL"
12 символов 063927396125            "Result is OK"
13 символов 1606700070967           "Result is OK"
18 символов 181930364906054831      "Result is OK"
19 символов 6458065268079694716     "Result is OK"
20 символов 25607246479550932530    "Result is FAIL"
```
* Пустая строка
```
""      "Result is FAIL"
```



### Тестирование производилось в следующем окружении:
* Windows 8.1 x64
*   Openjdk version "11.0.11" 2021-04-20

    OpenJDK Runtime Environment AdoptOpenJDK-11.0.11+9 (build 11.0.11+9);

    OpenJDK 64-Bit Server VM AdoptOpenJDK-11.0.11+9 (build 11.0.11+9, mixed mode)
* Формирование невалидных номеров

    *Python 3.8* [Файл](Luhn_and_generation.py)
    ```python
    from random impot randint

    def line(n=16):
        """
        Формирует рандомное (16значное по умолчанию) число в формате строки, верное по алгоритму Луна.
        """
        list = []
        for x in range(n-1):
            list.append(str(randint(0, 9)))
        
        summ = 0
        parity = n % 2 
        for i, digit in enumerate(list): 
            j = int(digit)
            if i % 2 == parity: 
                j *= 2 
                if j > 9: 
                    j -= 9
            summ += j

        if summ % 10 != 0:
            list.append(str(10 - (summ % 10)))
        else:
            list.append('0')
        return ''.join(list)

    for i in range(3):
        print (line())
    ```


