"""Simplified TCP Tahoe and Reno congestion-window illustration."""
def simulate(losses, ssthresh=16, reno=True, rounds=20):
    cwnd, trace = 1, []
    for rtt in range(1, rounds + 1):
        trace.append(cwnd)
        if rtt in losses:
            ssthresh = max(cwnd // 2, 2)
            cwnd = ssthresh if reno else 1
        elif cwnd < ssthresh:
            cwnd = min(cwnd * 2, ssthresh)
        else:
            cwnd += 1
    return trace

if __name__ == "__main__":
    for label, reno in (("Reno ", True), ("Tahoe", False)):
        trace = simulate({8, 14}, reno=reno)
        print(label, " ".join(f"{w:2d}" for w in trace),
              f"| segments sent {sum(trace)}")
    print("RTT 7 throughput:", 18 * 1460 * 8 / 0.040 / 1_000_000, "Mbps")
