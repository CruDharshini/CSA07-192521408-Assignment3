# Wireshark evidence guide
Use this folder for actual packet captures (.pcapng) and screenshots. No captures are fabricated or pre-created.

Suggested filters:
- TCP handshake: `tcp.flags.syn == 1 || tcp.flags.ack == 1`
- DNS: `dns`
- UDP: `udp`
- TLS: `tls`
- QUIC: `quic` (when Wireshark can dissect it)
- HTTP: `http` (for visible unencrypted HTTP only)

Capture loopback traffic for the local Python socket demo. Save the capture as `q1_socket_demo.pcapng` and add screenshots showing packet details. For HTTPS/TLS, packet payloads are encrypted; handshake metadata may be visible, but do not expect HTTP content without authorized session-key decryption.
