# Q3 – Why Does the Home Page Take 8 Seconds?
Assumptions: 1 HTML + 80 objects, RTT 50 ms, negligible transmission time.

| Mechanism | RTTs | Time |
|---|---:|---:|
| Non-persistent, one connection | 162 | 8.10 s |
| Persistent HTTP/1.1, no pipelining | 82 | 4.10 s |
| Persistent HTTP/1.1, pipelining | 3 | 0.15 s |
| Non-persistent, 6 parallel connections | 30 | 1.50 s |
| 8 bundles, non-persistent | 18 | 0.90 s |
| 8 bundles, persistent no pipelining | 10 | 0.50 s |

HTTP/2 multiplexes streams over one TCP connection but TCP packet loss can block delivery of later bytes across streams. HTTP/3 uses QUIC over UDP and independent stream delivery, so loss in one stream does not impose TCP-level cross-stream head-of-line blocking.

For repeat visits, Cache-Control: public, max-age=86400 lets the browser reuse fresh assets; ETag enables conditional revalidation (304 response). A CDN caches content near users. Bundling reduces request count but can invalidate more content on small updates; HTTP/2/3 retain granular assets.

The RTT calculator is in `q3_code.py`. For real evidence, use browser DevTools → Network, enable Protocol and Disable cache for first-visit tests, then repeat with cache enabled. Save screenshots in `evidence/`.
