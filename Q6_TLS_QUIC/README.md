# Q6 – Count the Round Trips Before the First Byte
For RTT=100 ms, assignment model:
- TCP + TLS 1.2: 1 RTT TCP + 2 RTT TLS = 3 RTT = 300 ms.
- TCP + TLS 1.3: 1 RTT TCP + 1 RTT TLS = 2 RTT = 200 ms.
- QUIC first connection: combined transport/crypto handshake = 1 RTT = 100 ms.
- QUIC 0-RTT resumption: eligible early data can be sent immediately (0 RTT wait), but is replayable.

Never send non-idempotent financial operations (transfer, payment, beneficiary changes, PIN changes) as 0-RTT early data. Use 1-RTT or later protected requests for state-changing operations. Read-only idempotent requests may be considered for early data with application safeguards.

QUIC connection IDs allow connection migration when a client network changes IP/port; path validation still occurs. If UDP/443 is blocked, fall back to HTTPS over TCP/TLS 1.3 (e.g. Alt-Svc or connection racing).

The calculator prints handshake delay. Optional evidence: `openssl s_client -connect example.com:443 -tls1_3` and Wireshark TLS/QUIC packet inspection. Actual server support varies.
