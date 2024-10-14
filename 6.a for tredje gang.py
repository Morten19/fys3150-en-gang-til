def thomas_algorithm(l, d, u, g):
    n = len(d)
    
    # Step 1: Forward elimination
    d_prime = [0] * n
    g_prime = [0] * n
    
    # Initial values
    d_prime[0] = d[0]
    g_prime[0] = g[0]
    
    for i in range(1, n):
        alpha = l[i-1] / d_prime[i-1]
        d_prime[i] = d[i] - alpha * u[i-1]
        g_prime[i] = g[i] - alpha * g_prime[i-1]
    
    # Step 2: Back substitution
    v = [0] * n
    v[n-1] = g_prime[n-1] / d_prime[n-1]
    
    for i in range(n-2, -1, -1):
        v[i] = (g_prime[i] - u[i] * v[i+1]) / d_prime[i]
    
    return v
