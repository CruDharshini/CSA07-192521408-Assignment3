"""Loopback chat socket plus simplified reproducible impaired-link model."""
import random
import socket
import threading

def simulate_channel(data_bytes, loss_rate=0.05, rtt_ms=200,
                    rate_bps=5_000_000, seed=42, mtu=1400):
    rng = random.Random(seed)
    packets = (len(data_bytes) + mtu - 1) // mtu
    retransmissions = 0
    for _ in range(packets):
        while rng.random() < loss_rate:
            retransmissions += 1
    # Simplified illustrative model: one initial RTT plus one RTT per
    # recovery batch. This is not a TCP/QUIC implementation or netem test.
    recovery_batches = retransmissions // max(1, packets // 4 + 1)
    elapsed_ms = (1 + recovery_batches) * rtt_ms
    elapsed_ms += len(data_bytes) * 8 / rate_bps * 1000
    return packets, retransmissions, round(elapsed_ms, 2)

def loopback_chat():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]
    response = []

    def worker():
        conn, _ = server.accept()
        with conn:
            message = conn.recv(1024).decode()
            conn.sendall(f"ACK_DOCTOR: Received '{message}'".encode())

    thread = threading.Thread(target=worker)
    thread.start()
    with socket.create_connection(("127.0.0.1", port)) as client:
        client.sendall(b"PATIENT_ID:1042|BP:120/80|URGENT")
        response.append(client.recv(1024).decode())
    thread.join()
    server.close()
    return response[0]

if __name__ == "__main__":
    print("Chat Socket Exchange:", loopback_chat())
    packets, retransmissions, elapsed = simulate_channel(
        b"X" * 250_000, loss_rate=0.05, rtt_ms=200
    )
    print(f"250 KB illustrative transfer: {packets} packets, "
          f"{retransmissions} retransmissions, {elapsed} ms")
