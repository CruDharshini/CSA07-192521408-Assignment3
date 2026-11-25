# CSA0715 – Computer Networks
## Assignment CO3: Analyse and Compare Core Network Protocols

**Student:** Dharshini  
**Register Number:** 192521408  
**Department:** Information Technology  
**Academic Year:** 2026–2027  
**Total Marks:** 50

## Q1 – Which Socket Gets the Segment? (7 Marks)

TCP uses a connection 4-tuple (source IP, source port, destination IP, destination port) to identify an established connection. Thus 49.37.2.8:50001 and 117.96.4.2:50000 are separate TCP connections to 203.0.113.5:443 even though the source port 50000 is reused by one client in another connection. A new SYN without an established match is handled by the TCP listening socket, which creates a connected socket after accept(). UDP is connectionless; datagrams addressed to 203.0.113.5:5004 arrive at the bound UDP socket, and recvfrom() provides the sender address to the application.

For a 100-byte payload over IPv4, UDP adds 20-byte IP and 8-byte UDP headers: 128 bytes total, so header share is 28/128×100=21.875%. TCP without options adds 20-byte IP and 20-byte TCP headers: 140 bytes total, so header share is 40/140×100=28.57%. TCP/TLS is suitable for scores and commentary because order and reliable delivery matter. UDP with RTP/WebRTC is suitable for live video because freshness and low delay matter more than retransmitting every lost packet.

The loopback program in Q1 demonstrates UDP request/reply and reliable TCP byte-stream delivery. Under packet loss, TCP retransmits and preserves ordered delivery, while ordinary UDP does not retransmit automatically. Application-level RTP/WebRTC can use concealment, FEC and selective feedback. Actual loss-injection measurements must be captured locally; the source does not fabricate a Wireshark trace.

## Q2 – Read the Congestion Window (7 Marks)

The supplied cwnd trace is 1,2,4,8,16,17,18,19,9,10,11,12,13,14,1,2,4. Initial ssthresh is 16 segments because growth changes from exponential to linear at 16. After RTT 8, cwnd 19 is halved to floor(19/2)=9, indicating triple-duplicate ACK recovery. After RTT 14, cwnd 14 resets to 1, indicating a retransmission timeout; the new threshold is floor(14/2)=7. This pattern identifies Reno: Tahoe would reset cwnd to 1 on both loss signals.

At RTT 7, cwnd=18, MSS=1460 bytes and RTT=40 ms. Throughput=18×1460×8/0.04=5.256 Mbps. AIMD fairness is encouraged because additive increase grows flows together and multiplicative decrease reduces their windows proportionally. CUBIC uses a cubic growth curve and is common for high-bandwidth paths. BBR estimates bottleneck bandwidth and propagation RTT, then paces traffic; it can be less sensitive to random non-congestion loss than loss-based Reno, but performance depends on the network and implementation.

The Python source compares simplified Tahoe and Reno traces. This is a teaching model, not a full TCP stack implementation.

## Q3 – Why Does the Home Page Take 8 Seconds? (7 Marks)

There are 81 objects (one HTML plus 80 objects) and RTT=50 ms. Non-persistent HTTP with one connection requires 2 RTT per object: 162 RTT=8.10 s. Persistent HTTP/1.1 without pipelining requires one TCP handshake, one HTML request/response and 80 sequential object request/response RTTs: 82 RTT=4.10 s. With pipelining, the model is 3 RTT=150 ms. Six parallel non-persistent connections require 2+2×ceil(80/6)=30 RTT=1.50 s. Bundling to eight objects gives 18 RTT=900 ms non-persistent or 10 RTT=500 ms persistent without pipelining.

HTTP/2 multiplexes streams over TCP, but loss of a TCP segment can hold later stream bytes until retransmission. HTTP/3 uses QUIC over UDP and independent stream delivery, avoiding TCP-level cross-stream head-of-line blocking. Cache-Control max-age lets repeat visits reuse fresh static assets; ETag supports conditional revalidation. A CDN serves content closer to users. Bundling reduces request count but may invalidate more assets when one component changes. Browser DevTools waterfall evidence should be captured locally for the actual website.

## Q4 – How Many Queries Reach the University's DNS Server? (7 Marks)

With 40 independent ISP resolvers and continuous lookups, authoritative queries per hour are approximately R×3600/TTL. At TTL=300 s, each resolver sends 12 queries/hour and all 40 send 480/hour. At TTL=30 s, each sends 120/hour and all send 4,800/hour. The number of students is less important because students behind the same recursive resolver share its cache.

The student sends a recursive query to the ISP resolver. The resolver performs iterative queries through root, .in, .ac.in and the simats.ac.in authoritative server. The assignment's example A record is 10.20.30.40. A and AAAA provide addresses, NS provides delegation, CNAME provides aliases and TXT stores text policy/verification data; MX is relevant for mail. DNS commonly uses UDP/53 and falls back to TCP when truncation/large responses require it or for zone transfers. A 24-hour TTL can preserve stale records for a day after migration. A 300-second TTL is a practical balance during result-day traffic. The Python program simulates this referral chain and a cache; it does not query the live university DNS.

## Q5 – When Will the Video Call Freeze? (6 Marks)

For M/M/1, μ=1000 packets/s, utilisation ρ=λ/μ, average number in system L=ρ/(1−ρ), and mean system time W=1/(μ−λ). At λ=500, 800, 900, 950 and 990 packets/s, W is 2, 5, 10, 20 and 100 ms respectively; L is 1, 4, 9, 19 and 99. At λ≥μ the queue is unstable. W exceeds 20 ms when λ>950 packets/s. At λ=450, W=1/550=1.82 ms; at λ=900, W=10 ms. Queueing-only delay increases from about 0.82 to 9 ms, roughly eleven times.

For a 1 MB decimal bucket, B=8 Mb. With token rate r=2 Mbps and backup send rate R=10 Mbps, maximum burst duration above token replenishment is B/(R−r)=8/8=1 second. DiffServ can classify video as EF (DSCP 46), interactive applications as AF, and backups as BE (DSCP 0). Shape backups and apply admission control to EF so strict priority does not starve other traffic. QoS manages congestion but does not create bandwidth.

## Q6 – Count the Round Trips Before the First Byte (6 Marks)

At RTT=100 ms, the assignment model gives TCP+TLS 1.2 three RTTs (300 ms), TCP+TLS 1.3 two RTTs (200 ms), and a first QUIC connection one RTT (100 ms). QUIC 0-RTT resumption permits eligible early data immediately, but early data is replayable. Money transfers, payments, beneficiary changes and PIN changes must not be sent as 0-RTT requests; restrict early data to safe, idempotent reads. QUIC connection IDs support migration when a device changes from Wi-Fi to 5G, although path validation still occurs. If UDP/443 is blocked, fall back to HTTPS over TCP/TLS 1.3. Use OpenSSL and Wireshark locally to capture actual negotiated protocol evidence.

## Q7 – Choose the Protocols from First Principles (10 Marks)

For rural telemedicine over 4G (100–300 ms RTT and up to 5% loss), use WebRTC with RTP/SRTP over UDP for live audio/video, including adaptive bitrate, jitter buffers and FEC. Use HTTPS/HTTP/3 over QUIC with TLS 1.3 for patient records and X-rays, with SHA-256 integrity checks. Use a persistent QUIC stream or WebSocket over TLS for ordered clinical chat. Use DNS over HTTPS with local caching for hospital service lookup.

At a 64 KiB TCP window and 300 ms RTT, maximum window-limited throughput is 65,536×8/0.3=1,747,627 bps, approximately 1.75 Mbps. A 10 MiB file at that rate takes approximately 48 seconds before overhead and loss. A larger effective window through TCP window scaling or a suitable QUIC congestion controller is needed for higher throughput.

Use a local caching resolver with a balanced TTL. Apply DiffServ: EF for real-time media, AF for interactive/important data and BE for background transfers. Shape bulk transfers to protect real-time traffic. The included Python implementation demonstrates a loopback TCP chat and an illustrative impaired-link calculation; it is not a real 4G emulator. A 5G upgrade can improve RTT and capacity where available, but benefits must be measured. Evaluate commercial video vendors using measured delay, jitter, loss resilience, encryption, data residency, retention and independent security audits.

## Overall Conclusion

TCP, UDP, HTTP, DNS, TLS and QUIC serve different application requirements. Reliable ordered data benefits from TCP or QUIC streams, while real-time media benefits from low-delay UDP-based transport and media-level loss handling. Caching, congestion control and QoS improve performance when configured for the traffic type. The supplied scripts provide reproducible analytical demonstrations; live packet captures, DevTools measurements and impairment tests must be performed and documented on the student's own system.
