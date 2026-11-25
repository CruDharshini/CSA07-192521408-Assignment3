# Practical evidence guide

Capture evidence from your own computer and save the original files. Do not submit screenshots or packet captures that were not actually produced by your tests.

## Q1 – Socket demonstration
- Run `python q1_sockets.py`.
- Capture loopback traffic in Wireshark.
- Save the capture as `q1_socket_demo.pcapng`.
- Useful filters: `tcp`, `udp`, `tcp.flags.syn == 1`.

## Q3 – HTTP measurements
- Open browser DevTools → Network.
- Enable the Protocol column and record the protocol, request count and waterfall.
- Capture a first load with cache disabled, then a repeat load with cache enabled.
- Save genuine screenshots in the evidence you submit separately.

## Q6 – TLS/QUIC
- Optional TLS check: `openssl s_client -connect example.com:443 -tls1_3`.
- In Wireshark, inspect ClientHello and ServerHello records where visible.
- QUIC commonly uses UDP/443. Decryption requires appropriate session secrets; never share private keys or credentials.

## Q7 – Telemedicine
- Run `python q7_telemedicine.py` for the loopback chat and illustrative link model.
- The script is not a real 4G emulator. Optional Linux `tc netem` testing must be performed locally and recorded with the actual settings.

## General evidence
Record the date, operating system, Python version, application version, test target and any limitations. Keep raw captures and terminal output unchanged.
