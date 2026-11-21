# Q1 – Which Socket Gets the Segment?
TCP server sockets are demultiplexed by the connection 4-tuple (source IP, source port, destination IP, destination port); a new SYN with no matching established connection is handled by the listening socket. A UDP socket bound to a local address and port receives datagrams for that destination; the application uses recvfrom() to inspect each sender.

For the supplied server 203.0.113.5:
- TCP from 49.37.2.8:50001 → 203.0.113.5:443 maps to that client's established socket.
- TCP from 117.96.4.2:50000 → 203.0.113.5:443 maps to a different established socket.
- New SYN from 106.51.7.7:41000 → port 443 is accepted by the listening socket.
- UDP to 203.0.113.5:5004 is delivered to the shared UDP socket.

A 100-byte payload with IPv4 headers: UDP total = 20+8+100 = 128 bytes; TCP minimum total = 20+20+100 = 140 bytes (TCP options can increase the header). Header share of total is 21.875% for UDP and 28.57% for minimum TCP.

Use TCP/TLS for scores and commentary requiring ordered reliable delivery; use RTP/WebRTC over UDP for delay-sensitive live video where limited loss can be concealed or recovered with FEC.
