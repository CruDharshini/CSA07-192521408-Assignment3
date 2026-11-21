"""Handshake RTT model from the assignment."""
RTT_MS = 100
protocols = {
    "TCP + TLS 1.2": 3,
    "TCP + TLS 1.3": 2,
    "QUIC first connection": 1,
    "QUIC 0-RTT resumption (eligible early data)": 0,
}
for name, rtts in protocols.items():
    print(f"{name:44} {rtts} RTT  {rtts * RTT_MS} ms")
print("Warning: 0-RTT early data is replayable; do not use for state-changing transactions.")
