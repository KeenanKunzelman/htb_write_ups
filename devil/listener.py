#!/usr/bin/env python

import socket



def main():
  bind_ip = "10.0.0.59"
  bind_port = 4444

  shell_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  shell_listener.bind((bind_ip, bind_port))
  shell_listener.listen(5)

  while True:
    client,addr = shell_listener.accept()




if __name__ == "__main__":
  main()

