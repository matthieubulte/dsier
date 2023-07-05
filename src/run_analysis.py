if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    from pyfrechet.metric_spaces import MetricData, CorrFrobenius
    
    M = CorrFrobenius(dim=10)

    def bootstrap(mats, s, n, estimator):
        N = mats.shape[0]
        hats = np.zeros(n)
        for i in tqdm(range(n)):
            idx = np.random.permutation(N)[:s]
            bmats = mats[idx,:,:]
            hats[i] = estimator(bmats)
        return hats

    def m(x, theta, mu):
        return M._frechet_mean(np.array([x, mu]), np.array([theta, 1-theta]))

    def alpha_hat(x):
        tgrid = np.linspace(0,1,100)
        mu_hat = MetricData(M, x).frechet_mean()
        def calc(_theta): return np.array([ M._d(m(x[j-1,:], _theta, mu_hat), x[j,:])**2 for j in range(1, x.shape[0]) ]).mean()
        errs = np.array([ calc(tgrid[i]) for i in range(tgrid.shape[0]) ])
        return tgrid[np.argmin(errs)]

    mats = np.load("./data/matrices_ts.npy")
    N = mats.shape[0]

    print("#" * 20)
    print("Bootstraping distribution of hat alpha under H0")
    alpha_hats = bootstrap(mats, 40, 500, alpha_hat)

    print("#" * 20)
    print("Computing alpha hat")
    est = alpha_hat(mats)
    q_95 = np.quantile(alpha_hats, 0.95)

    print("#" * 20)
    print("Plotting results")
    
    # Eigenvals
    evals = np.zeros((N, M.dim))
    for i in range(N):
        evals[i,:] = np.sort(np.linalg.eigvals(mats[i,:,:]))

    plt.plot(np.arange(N), np.log10(evals[:,0]), color='black', label=r'$\log_{10}(\lambda_{it})$')
    for i in range(1,M.dim):
        plt.plot(np.arange(N), np.log10(evals[:,i]), color='black')
    plt.legend()
    plt.savefig('./output/timeseries.pdf')

    # Alpha
    plt.clf()
    plt.axvline(est, color='black', label=f"alpha; {est:.2f}")
    plt.axvline(q_95, color='black', linestyle='--', label=f"q_95: {q_95:.2f}")
    plt.hist(alpha_hats, color='black', alpha=0.5, density=True,bins=20)
    plt.legend()
    plt.savefig('./output/result.pdf')

