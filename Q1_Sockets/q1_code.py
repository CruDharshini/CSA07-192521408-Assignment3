"""Loopback TCP and UDP socket demonstration; standard library only."""
import socket
import threading

def udp_server(sock):
    for _ in range(3):
        data, addr = sock.recvfrom(1024)
        sock.sendto(b"ACK:" + data, addr)

def tcp_server(sock, result):
    conn, _ = sock.accept()
    with conn:
        total = 0
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            total += len(chunk)
    result.append(total)

def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("127.0.0.1", 0))
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(("127.0.0.1", 0))
    tcp.listen(1)

    udp_thread = threading.Thread(target=udp_server, args=(udp,))
    tcp_result = []
    tcp_thread = threading.Thread(target=tcp_server, args=(tcp, tcp_result))
    udp_thread.start()
    tcp_thread.start()

    for name in ("lab1", "lab2", "lab3"):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.sendto(name.encode(), udp.getsockname())
            reply, _ = client.recvfrom(1024)
            print("UDP", name, "->", reply.decode())

    with socket.create_connection(tcp.getsockname()) as client:
        client.sendall(b"x" * 100_000)

    udp_thread.join()
    tcp_thread.join()
    print(f"TCP server received {tcp_result[0]} bytes in order")
    udp.close()
    tcp.close()

if __name__ == "__main__":
    main()
