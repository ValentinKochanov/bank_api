Стек:

    Python >= 3.8
    Django >= 3.1.1
    Djangorestframework >= 3.11.1
    SQLite3
    
Сделать сервис по принципам RESTful API. Представим, что мы делаем API для банка (в миниатюре) для партнеров. Функционал следующий:


1. Выпуск банковской карты (генерируется номер виртуальной банковской карты и номер счета)
   * Запрос: выпуск карты, ФИО, номер телефона, id пользователя
   * Ответ: номер сгенерированной карты, техническая информация (время, ip-адрес и т.д.)
2. Проверка баланса карты
   * Запрос: номер карты
   * Ответ: баланс карты
3. Зачисление суммы на карту. Процесс зачисления выглядит как перевод средств с мастер-счета на счет выпущенной ранее карты
   * Запрос: номер карты, сумма зачисления
   * Ответ: подтверждение успешного перевода, время 
4. Списание денег с карты
   * Запрос: Кто списывает (ИНН-организации), сколько списывает (с т.з. механики просто удаляем эти деньги из системы, или переводим на отдельный счет «для компаний»), время операции.
   * Ответ: формирование письма на email клиента (указать любой ящик) с чеком операции
5. Запросить историю транзакций по карте
   * Запрос: запросить N последних транзакций
   * Ответ: список транзакций


Если будет время и желание, сделать web-интерфейс абстрактного администратора системы который может: 
* посмотреть список выпущенных карт, 
* историю транзакций по каждой карте, 
* статистику системы
* завести «деньги» на мастер-счет, 
* настроить систему (указать email, завести компании через добавление ИНН) и т.д. 


Выбор и глубина проработки функций - на усмотрение и желание разработчика. 


Язык – python3. БД и Фреймворки, библиотеки можно использовать любые.
