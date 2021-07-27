# КЛИЕНТСКАЯ ЧАСТЬ
import socket


def client_program():  # именная функция
    # присваиваем переменной host строку, содержащую имя хоста компьютера,
    # на котором в настоящее время выполняется интерпретатор Python
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # инициируем номер порта (5000)
    client_socket = socket.socket()  # создание сокета
    client_socket.connect((host, port))  # связываем сокет с хостом и портом
    message = input(" -> ")  # ввод
    # цикл работает пока не получен 'bye'
    while message.lower().strip() != 'bye':  # lower() - в нижний регистр; strip() - удаляем пробелы
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
