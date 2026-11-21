# Q4 – How Many Queries Reach the University's DNS Server?
For continuous lookups with R distinct recursive resolvers, the approximate authoritative query rate is R×3600/TTL queries per hour. For 40 resolvers:
- TTL 300 s: 12 queries/hour/resolver; 480 total/hour.
- TTL 30 s: 120 queries/hour/resolver; 4,800 total/hour.
Student count is less important than the number of independent caching resolvers and TTL while caches remain warm.

Student-to-ISP lookup is recursive. The ISP resolver follows iterative referrals through root, .in, .ac.in and the simats.ac.in authoritative server. The supplied teaching model returns A=10.20.30.40. A, AAAA, NS, CNAME and TXT are common record types; MX is needed if mail is handled for the name. DNS commonly uses UDP/53; TCP/53 is used for zone transfers and when truncated/large responses require fallback.

A long TTL such as 86,400 s can keep stale addresses cached for up to a day after migration. A moderate TTL such as 300 s balances cache efficiency and failover agility. The Python program simulates referrals and a TTL cache; it is not a live query to the university DNS.
