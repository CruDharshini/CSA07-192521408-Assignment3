# Q7 – End-to-End Rural Telemedicine Design

| Traffic | Protocol choice | Main requirement |
|---|---|---|
| Live consultation video/audio | WebRTC with RTP/SRTP over UDP; FEC/adaptive bitrate | Low delay/jitter; tolerate limited loss |
| Patient records and X-rays | HTTPS / HTTP/3 over QUIC with TLS 1.3; integrity hash | Reliable ordered object transfer and integrity |
| Clinical chat | Persistent QUIC stream or WebSocket over TLS | Reliable ordered messages |
| Hospital service lookup | DoH with local caching; DNSSEC validation where supported | Private, reliable name lookup |

At 64 KiB window and 300 ms RTT, theoretical window-limited TCP throughput is 65,536×8/0.3 = 1.747 Mbps. A 10 MiB transfer at that ideal rate takes about 48 seconds before protocol overhead/loss. Window scaling or a larger effective window is needed to use higher capacity.

For rural 4G (100–300 ms RTT, up to 5% loss), use local DNS caching, traffic classification and QoS: EF for real-time media, AF for interactive/important data, and BE for background transfers. QoS cannot create capacity; shape background traffic and monitor queue delay.

Stage 3 code provides a real loopback TCP chat exchange and a reproducible packet-loss/serialization teaching model for a 250 KB file. It does not emulate a real cellular network. Linux `tc netem` tests are optional and require local execution.

A 5G upgrade may reduce latency and improve capacity where coverage and deployment permit; it is not guaranteed. Evaluate a third-party video vendor using measured glass-to-glass delay, jitter, loss resilience, encryption, data residency, retention and independent security audits before adoption.
