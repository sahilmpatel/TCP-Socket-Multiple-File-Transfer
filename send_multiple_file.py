import socket
import os

HOST, PORT = "192.168.29.44", 9999


class SendFiles:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.file_names = []
        self.file_paths = []
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def file_input(self):
        """
        Enter full path along with a filename
        e.g. G:\soceket programmming\test.py, G:/soceket programmming/pic_2.png

        file_names list contains tuple of filename and file-size.
        """
        for _ in range(int(input("Number of files to share:"))):
            file_path = input("Enter file name:")
            self.file_paths.append(file_path)
            self.file_names.append((os.path.basename(file_path), os.stat(file_path).st_size))
        return self.file_paths, self.file_names

    def operation(self):
        """
        Steps:
            1. Send the filename along with size (file_names list).
            2. Send the file until EOF is reached by using socket.sendfile() method.
               file must be a regular file object opened in binary mode.
        """
        with self.soc:
            self.soc.connect((self.host, self.port))
            path_list, names_list = self.file_input()
            self.soc.send(str(names_list).encode('utf-8'))
            for path in path_list:
                with open(path, 'rb') as f:
                    self.soc.sendfile(f, 0)
            print(self.soc.recv(1024).decode('utf-8').upper())


send_op = SendFiles(HOST, PORT)
send_op.operation()
