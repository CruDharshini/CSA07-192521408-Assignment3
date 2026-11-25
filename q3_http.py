"""Calculate the assignment's page-load RTT models."""
RTT_MS = 50
objects = 80
models = {
    "Non-persistent, one connection": 2 * (1 + objects),
    "Persistent HTTP/1.1, no pipelining": 2 + objects,
    "Persistent HTTP/1.1, pipelining": 3,
    "Non-persistent, 6 parallel connections": 2 + 2 * ((objects + 5) // 6),
    "8 bundles, non-persistent": 2 * (1 + 8),
    "8 bundles, persistent no pipelining": 2 + 8,
}
for name, rtts in models.items():
    print(f"{name:42} {rtts:3} RTTs  {rtts * RTT_MS:5} ms")
