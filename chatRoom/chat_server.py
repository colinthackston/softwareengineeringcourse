import socket, threading, sys, pickle


class Server:
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 5002,
        nickname: str = "Server",
        buffer_recv: int = 4097,
        max_socket_conn: int = 10,
    ):
        self.clients = []
        self.buffer_recv = buffer_recv
        self.nickname = nickname
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind((host, port))
        self.socket.listen(max_socket_conn)
        self.socket.setblocking(False)

        accept_conn_thread = threading.Thread(target=self.accept_connection)
        accept_conn_thread.daemon = True
        accept_conn_thread.start()

        process_conn_thread = threading.Thread(target=self.process_connection)
        process_conn_thread.daemon = True
        process_conn_thread.start()

    def accept_connection(self):
        while True:
            try:
                conn, addr = self.socket.accept()
                conn.setblocking(False)
                self.clients.append(conn)
                print("\n\t\t- New user connection -\n")
            except:
                pass

    def process_connection(self) -> None:
        print("\t\t***** Server starting ******\n")

        while True:
            for client in self.clients:
                try:
                    data = self.get_data(client)

                    if data:
                        self.send_msg_to_all(client, data)
                        self.print_msg(data)
                except:
                    pass

    def get_data(self, client=None) -> str:
        return client.recv(self.buffer_recv)

    def print_msg(self, data: str) -> None:
        nickname, msg = self.parse_msg(data)
        print("\n<{}> {}".format(nickname, msg))

    def parse_msg(self, data: str) -> str:
        return pickle.loads(data)

    def send_msg_to_all(self, client=None, data: str = None) -> None:
        for c in self.clients:
            try:
                if c != client:
                    c.send(self.parse_data(data) if client is None else data)
            except:
                self.clients.remove(c)

    def parse_data(self, msg: str) -> str:
        return pickle.dumps((self.nickname, msg))

    def close(self):
        self.socket.close()


def main():
    nickname = "Server"
    server = Server(nickname=nickname)

    while True:
        msg = input("<Server>: ")

        if msg.lower() != "exit":
            server.send_msg_to_all(data=msg)
            print("<Server>:", msg)
        else:
            server.close()
            break


if __name__ == "__main__":
    main()
