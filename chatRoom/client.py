import socket, threading, sys, pickle


class Client:
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 5002,
        nickname: str = None,
        buffer_recv: int = 4097,
    ):
        self.buffer_recv = buffer_recv
        self.nickname = nickname
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((host, port))

        msg_thread = threading.Thread(target=self.process_messages)
        msg_thread.daemon = True
        msg_thread.start()

    def process_messages(self) -> None:
        print("\t\t***** Welcome {}! :) *****\n".format(self.nickname))

        while True:
            try:
                data = self.get_data()

                if data:
                    self.print_msg(data)
            except:
                pass

    def get_data(self) -> str:
        return self.socket.recv(self.buffer_recv)

    def print_msg(self, data: str) -> None:
        nickname, msg = self.parse_msg(data)
        print("\n<{}> {}".format(nickname, msg))

    def parse_msg(self, data: str) -> tuple:
        return pickle.loads(data)

    def send_msg(self, msg: str) -> None:
        self.socket.send(self.parse_data(msg))

    def parse_data(self, msg: str) -> str:
        return pickle.dumps((self.nickname, msg))

    def close(self) -> None:
        self.socket.close()


def main():
    nickname = input("Name: ").strip()

    client = Client(nickname=nickname)

    while True:
        msg = input("<{}>: ".format(nickname))

        if msg.lower() != "exit":
            client.send_msg(msg)
        else:
            client.close()
            break


if __name__ == "__main__":
    main()
