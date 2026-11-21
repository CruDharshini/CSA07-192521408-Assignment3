# Q5 – When Will the Video Call Freeze?
M/M/1 assumptions: Poisson arrivals, exponential service, one server, stable queue λ<μ, μ=1000 packets/s. Utilisation ρ=λ/μ, mean number in system L=ρ/(1−ρ), mean system time W=1/(μ−λ).

| λ (pkt/s) | ρ | L | W |
|---:|---:|---:|---:|
| 500 | 0.50 | 1 | 2 ms |
| 800 | 0.80 | 4 | 5 ms |
| 900 | 0.90 | 9 | 10 ms |
| 950 | 0.95 | 19 | 20 ms |
| 990 | 0.99 | 99 | 100 ms |
| 1000 | 1.00 | Unstable | Unbounded |

W exceeds 20 ms when λ>950 pkt/s. At λ=450, W=1/550=1.82 ms; at λ=900, W=10 ms. The queueing-only delay Wq=L/λ=ρ/(μ−λ) rises from about 0.82 ms to 9 ms (about 11×).

Token bucket: B=1 decimal MB=8 Mb, token rate r=2 Mbps, backup rate R=10 Mbps. Burst duration while sending above token rate: B/(R−r)=8/8=1 second.

DiffServ: video EF (DSCP 46) with strict priority and admission control; interactive web/ERP AF class with reserved minimum; backups BE (DSCP 0), shaped/policed to avoid starving real-time traffic. Strict priority needs safeguards to prevent starvation.
