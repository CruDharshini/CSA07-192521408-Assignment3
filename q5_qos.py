"""M/M/1 metrics and token-bucket burst calculations."""
def mm1(lam, mu):
    if lam >= mu:
        return None
    rho = lam / mu
    L = rho / (1 - rho)
    W = 1 / (mu - lam)
    return rho, L, W

if __name__ == "__main__":
    mu = 1000
    for lam in (500, 800, 900, 950, 990, 1000):
        result = mm1(lam, mu)
        if result is None:
            print(f"load {lam:4d} pkt/s: unstable, queue grows without limit")
        else:
            rho, L, W = result
            print(f"load {lam:4d} pkt/s: rho {rho:.2f} L {L:6.1f} pkts "
                  f"W {W * 1000:6.1f} ms")
    bucket_bits, token_rate, send_rate = 8_000_000, 2_000_000, 10_000_000
    print("Token-bucket burst duration:",
          bucket_bits / (send_rate - token_rate), "seconds")
