# СЕРВЕРНАЯ ЧАСТЬ
import socket


def server_program():  # именная функция
    # присваиваем переменной host строку, содержащую имя хоста компьютера,
    # на котором в настоящее время выполняется интерпретатор Python
    host = socket.gethostname()
    port = 5000  # инициируем номер порта (5000)
    server_socket = socket.socket()  # создание сокета
    server_socket.bind((host, port))  # связываем сокет с хостом и портом
    # запуск режима прослушиания кол-во клиентов, которых облужиает сервер одновременно - 2 шт.
    server_socket.listen(1)
    # принять подключение, возвращает кортеж с двумя элементами: новый сокет и адрес клиента
    conn, address = server_socket.accept()  # вот здесь оно останавлиается

    # Вывод о соединении
    print("Connection from: " + str(address))

    while True:  # бесконечный цикл пока не возникнет break
        # контроль объема пакетов получения данных recv(1024) не больше 1024 байта
        # decode() - возвращает строку, декодированную из заданных байтов
        data = conn.recv(1024).decode()
        if not data:  # если данные не получены break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # отправить данные клиенту
    conn.close()  # закрыть соединение


if __name__ == '__main__':
    server_program()  # запуск функции как основного модуля


# Источник: https://pythonim.ru/osnovy/sokety-v-python
