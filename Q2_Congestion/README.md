# Q2 – Read the Congestion Window
Given cwnd trace at RTT 1–17: 1,2,4,8,16,17,18,19,9,10,11,12,13,14,1,2,4.

- Initial ssthresh = 16 segments: exponential slow start changes to linear growth at 16.
- Loss after RTT 8: cwnd 19; ssthresh = floor(19/2) = 9. The immediate reduction to 9 followed by linear growth indicates triple-duplicate-ACK recovery in Reno.
- Loss after RTT 14: cwnd 14; timeout resets cwnd to 1; ssthresh = floor(14/2) = 7.
- Variant: TCP Reno. Tahoe would reset cwnd to 1 after triple duplicate ACKs too.
- RTT 7 cwnd = 18, MSS = 1460 B, RTT = 0.04 s. Throughput = 18×1460×8/0.04 = 5.256 Mbps.

AIMD fairness: additive increase moves flows by similar increments; multiplicative decrease reduces each window proportionally, tending toward a fair sharing line under a shared bottleneck.

CUBIC uses a cubic window-growth function and is designed for high-bandwidth, long-distance paths. BBR estimates bottleneck bandwidth and minimum RTT and paces traffic; it does not rely on packet loss as its primary congestion signal. BBR can help where random wireless loss is not congestion, though real results depend on implementation and network conditions.
