# CSA0715 – Computer Networks | Assignment CO3
**Student:** Dharshini  
**Register number:** 192521408  
**Department:** Information Technology  
**Academic year:** 2026–2027  
**Total:** 50 marks | Individual assignment

## CO3 coverage
TCP, UDP, sockets, demultiplexing, congestion control, HTTP/1.1–HTTP/3, caching, DNS, TTL, queuing, QoS, TLS 1.2/1.3, QUIC and end-to-end protocol selection.

## Repository layout
- `Q1_Sockets/` – TCP/UDP socket demo and demultiplexing notes
- `Q2_Congestion/` – Tahoe/Reno cwnd simulation
- `Q3_HTTP/` – HTTP page-load RTT calculator and browser test guide
- `Q4_DNS/` – iterative DNS hierarchy and TTL cache simulator
- `Q5_QoS/` – M/M/1 queue, token bucket and QoS calculations
- `Q6_TLS_QUIC/` – handshake RTT calculator and Wireshark/OpenSSL guide
- `Q7_Telemedicine/` – socket transfer, impaired-link model and design
- `Report/` – consolidated written answers

## Requirements
Python 3.10 or later (standard library only). Wireshark and OpenSSL are optional for packet inspection. Linux is needed for the documented `tc netem` commands; Windows users can use WSL2. Chrome/Edge DevTools can be used for HTTP observations.

## Run the programs
From the repository root:
```bash
python Q1_Sockets/q1_code.py
python Q2_Congestion/q2_code.py
python Q3_HTTP/q3_code.py
python Q4_DNS/q4_code.py
python Q5_QoS/q5_code.py
python Q6_TLS_QUIC/q6_code.py
python Q7_Telemedicine/q7_code.py
```
On Windows, use `py` instead of `python` if needed.

## Evidence and honesty note
The Python programs are source artifacts and can be run locally. Packet captures, DevTools waterfalls, `tc netem` measurements, OpenSSL output and screenshots must be captured on the student's machine. The repository does not claim that those external experiments were performed. Save actual evidence in each task's `evidence/` folder after testing.

Fill in the exact operating-system, Python, Wireshark and OpenSSL versions used before submission. Commit task work progressively; do not fabricate measurements or screenshots.
