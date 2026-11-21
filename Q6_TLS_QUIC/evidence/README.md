# TLS/QUIC evidence
Optional checks:
- Run `openssl s_client -connect example.com:443 -tls1_3` and save the actual negotiated protocol/cipher output.
- In Wireshark, capture the connection and inspect ClientHello, ServerHello and TLS 1.3 handshake records where visible.
- QUIC traffic may be identified as UDP/443; decryption requires suitable session secrets.
- Record date, target host, tool versions and any limitations. Never paste private keys or credentials.
