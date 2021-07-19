# Отчёт о тестировании Credit Card Number Validator

## Краткое описание

10.07.2021 было проведено функциональное модульное тестирование приложения Credit Card Number Validator. Проводилось тестирование новой функциональности - позитивные, негативные сценарии.

На тестирование затрачено: 4 часа

### В результате тестирования выявлены следующие дефекты:
* [Номера валидных карт длиной 19, 15, 14 символов не валидируются](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/1)

* [Номер невалидной карты длиной 16 символов валидируется](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/3)

* [Специальные символы длиной 16 символов вызывают ошибку работы программы](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/4)

* [Номера карт нестандарной длины не валидируются](https://github.com/senselessmessinspace/task_1-1_Credit_Card_Number_Validator/issues/5)

## Описание процесса тестирования

В процессе тестирования использовались следующие артефакты:
* [чек-лист тестирования](CHECK_LIST.md)
* Набор тестовых данных

### В качестве тестовых данных использовались данные:
* Валидные номера кредитных карт:
    * [Генератор номеров кредитных карт](https://www.freeformatter.com/credit-card-number-generator-validator.html#cardFormats)
```
Номер карты             Ожидаемый результат
---------------------------------------------
VISA:                   
4929381172299319        "Result is OK"
4556797771617249        "Result is OK"
4024007177934802088     "Result is OK"
---------------------------------------------
MasterCard:
5433315306974765        "Result is OK"
5523970037553162        "Result is OK"
5299312766351033        "Result is OK"
---------------------------------------------
American Express (AMEX):
375888213791754         "Result is OK"
372934484746193         "Result is OK"
342472795059854         "Result is OK"
---------------------------------------------
Discover:
6011047178167123        "Result is OK"
6011307146481026        "Result is OK"
6011271554929444486     "Result is OK"
---------------------------------------------
JCB:
3529110574258391        "Result is OK"
3543337443952654        "Result is OK"
3537343607919471660     "Result is OK"
---------------------------------------------
Diners Club - North America:
5591486859958444        "Result is OK"
5554410896547429        "Result is OK"
5423577014567155        "Result is OK"
---------------------------------------------
Diners Club - Carte Blanche:
30224097611701          "Result is OK"
30591078654524          "Result is OK"
30297593444751          "Result is OK"
---------------------------------------------
Diners Club - International:
36598868475261          "Result is OK"
36170740477350          "Result is OK"
36736565794549          "Result is OK"
---------------------------------------------
Maestro:
5020609834079348        "Result is OK"
5018381749595917        "Result is OK"
5038454146170315        "Result is OK"
---------------------------------------------
Visa Electron:
4844296619792332        "Result is OK"
4913709993273345        "Result is OK"
4026381141621082        "Result is OK"
---------------------------------------------
InstaPayment:
6382781034400044        "Result is OK"
6373786956379994        "Result is OK"
6374167479824767        "Result is OK"
```
* Невалидные номера кредитных карт: 16 символов, цифры, верные по алгоритму Луна, но не являются номерами карт (неверный BIN).
    * [Проверка валидности номера карты #1](http://validate.creditcard/) 
    * [Проверка валидности номера карты #2](https://www.creditcardvalidator.org/validator) 
    * [Проверка валидности номера карты #3](https://cardgenerator.io/credit-card-validator/)
```
Номер карты             Ожидаемый результат
---------------------------------------------
7293790973691683        "Result is FAIL"
0908835666806445        "Result is FAIL"
0962241471513826        "Result is FAIL"
3277486371341505        "Result is FAIL"
2215611035909754        "Result is FAIL"
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


