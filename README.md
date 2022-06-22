# Optimize holdings 

This repository contains scripts (in the `main` branch) and files (in the `gh-pages` branch) for optimizing stock holdings and an online article respectively.

## The article 

Please see [here](https://kshkb.github.io/Optimize-two-normal-randoms/bgtheory.html) for the article, hosted through GitHub pages.

This article describes the theory and derivation underlying the methods in our optimization program in the `main` branch. It is essentially a mean-variance type analysis for portfolios of two securities (c.f., the [Mutual fund seperation theorem](https://en.wikipedia.org/wiki/Mutual_fund_separation_theorem)). 

## The program

On running `main.py`, the user is prompted to enter the following information:

- the stock ticker codes to be analyzed;
- the starting and ending dates specifying the *time range* over which to analyze;
- an initial investment amount;
- the number of time periods into which to divide the specified time range;

After entering in this information, statistics are generated and printed on the screen. They report the (annualized) growth rate and standard deviation for each stock. The user is then prompted to specify their risk tolerance (understood as a desired standard deviation in their portfolio comprised of each stock).

The program `main.py` then returns the optimal amount the user ought to hold or short in their first and second stock. These are the suggested holdings for the user in order to maximize their portfolio growth at the specified risk tolerance.

### Important preliminary information

As in the author's repository `stock-performance-analysers`, the scripts in this repository call on the IEX cloud API (see [here](https://iexcloud.io/)).

In order to run these scripts you need to edit the file `secrets.py` and update the values `IEX_ClOUD_SANDBOX` or `IEX_CLOUD_API_TOKEN` with a valid API token from IEX cloud.

You can make an account and buy tokens on IEX Cloud.

**Note.** *Sandbox environment tokens are free!*

#### Environments

Each script in this repository is set to run in the sandbox environment. This means the data accessed to measure stock performance is not real world data. Rather, it is a randomized version that loosely approximates real world data. As noted above, sandbox environment tokens are freely available from IEX Cloud.

In order to run the modules in this repository on real world data you need to:

- comment out the line `os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'` in the module `getstats.py`;
- in the `getstats.py` module, in the method `returnStatistics()`, replace all instances of `token=IEX_CLOUD_SANDBOX` with `token=IEX_CLOUD_API_TOKEN`.







