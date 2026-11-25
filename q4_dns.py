"""Small iterative DNS hierarchy and TTL-cache teaching simulation."""
import time

SERVERS = {
    "root": {"in.": "tld-in", "com.": "tld-com"},
    "tld-in": {"ac.in.": "ns-ac"},
    "tld-com": {"example.com.": "ns-example"},
    "ns-ac": {"simats.ac.in.": "ns-simats"},
    "ns-simats": {"results.simats.ac.in.": "10.20.30.40"},
    "ns-example": {"www.example.com.": "93.184.216.34"},
}
CACHE_TTL = 300
cache = {}

def resolve(name, now=None):
    now = time.time() if now is None else now
    cached = cache.get(name)
    if cached and now < cached[1]:
        return cached[0], 0

    server, queries = "root", 0
    while True:
        queries += 1
        matches = [suffix for suffix in SERVERS[server] if name.endswith(suffix)]
        if not matches:
            raise LookupError(f"No referral for {name} at {server}")
        suffix = max(matches, key=len)
        answer = SERVERS[server][suffix]
        if answer.replace(".", "").isdigit():
            cache[name] = (answer, now + CACHE_TTL)
            return answer, queries
        server = answer

if __name__ == "__main__":
    for domain in ("results.simats.ac.in.", "www.example.com.",
                   "results.simats.ac.in."):
        ip, count = resolve(domain)
        print(f"{domain:<24} {ip:<15} queries sent: {count}")
    print("TTL query rates for 40 resolvers:")
    for ttl in (300, 30):
        print(f"TTL {ttl:3}s: {3600 // ttl:3} per resolver, "
              f"{40 * 3600 // ttl:5} total per hour")
