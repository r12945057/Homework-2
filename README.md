# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution  
    path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129889  
    tokenB->tokenA, amountIn=5, amountOut=5.655321988655322  
    tokenA->tokenD, amountIn=5.655321988655322, amountOut=2.4587813170979333  
    tokenD->tokenC, amountIn=2.4587813170979333, amountOut=5.0889272933015155  
    tokenC->tokenB, amountIn=5.0889272933015155, amountOut=20.129888944077443

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution  
    Slippage in AMM refers to the difference between the expected price of a token swap and the actual price at which the trade is executed. Uniswap V2 incorporates a mechanism to set a tolerance limit. When swapping tokens on Uniswap V2, users can specify a maximum acceptable slippage percentage. This value essentially determines how much deviation from the expected price they're willing to accept for the trade to be executed. If the actual price falls within the user-defined slippage range, the swap proceeds. Otherwise, the transaction reverts, protecting the user from excessive price deviations.

    ```python
    def uniswap_v2_swap(reserve_in, reserve_out, amount_in):
    """
    Simulates a swap on a Uniswap V2-like AMM with constant product reserves.

    Args:
        reserve_in: The initial reserve of the token being provided (e.g., ETH).
        reserve_out: The initial reserve of the token being received (e.g., DAI).
        amount_in: The amount of the input token being provided.

    Returns:
        The amount of the output token received.
    """
    # Constant product formula before the swap
    constant_product = reserve_in * reserve_out

    # Amount of output token received
    amount_out = amount_in / (amount_in + reserve_in) * reserve_out

    # Update reserves after the swap (for simulation purposes only)
    reserve_in += amount_in
    reserve_out -= amount_out

    return amount_out

    # Example usage
    reserve_in = 1000  # ETH
    reserve_out = 10000  # DAI
    amount_in = 1  # ETH

    amount_out = uniswap_v2_swap(reserve_in, reserve_out, amount_in)

    print(f"Swapping {amount_in} ETH for approximately {amount_out} DAI")

    # Slippage: Difference between expected output based on constant product and actual output
    expected_output = reserve_out * amount_in / (reserve_in + amount_in)
    slippage = (expected_output - amount_out) / expected_output * 100

    print(f"Slippage: {slippage:.2f}%")
    ```

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution  
    In the UniswapV2Pair contract, the mint function is responsible for minting liquidity tokens when liquidity is added to the pair. One important aspect of this function is that it subtracts a minimum liquidity amount from the liquidity tokens minted. This minimum liquidity requirement ensures that users cannot create extremely small liquidity positions that may not be economically viable for the functioning of the AMM. First, in AMMs like Uniswap, the price of an asset is determined by the ratio of the two assets in the liquidity pool. Extremely small liquidity positions can be highly sensitive to price fluctuations, leading to significant slippage for trades involving these positions. By requiring a minimum liquidity amount, the AMM ensures that liquidity providers have a sufficient stake in the pool to mitigate price sensitivity.Second, extremely small liquidity positions can lead to inefficiencies in trading, as they may not provide enough liquidity depth to accommodate larger trades without significant price impact. Requiring a minimum liquidity amount helps maintain a certain level of trading efficiency by ensuring there is enough liquidity in the pool to handle trades of various sizes.In addition, having a minimum liquidity requirement also contributes to the stability and robustness of the AMM protocol. It reduces the likelihood of manipulative or spammy behavior by discouraging users from creating excessively small liquidity positions that could disrupt the functioning of the protocol. The rationale behind this design decision is mainly to prevent users from creating liquidity positions that could potentially cause issues with price discovery and trading in the AMM.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution  
    The minting function within the UniswapV2Pair contract controls how liquidity tokens are minted when users deposit tokens into a liquidity pool. This function employs a specific formula to determine the amount of liquidity tokens that should be minted based on the quantities of the two tokens being deposited. The intention behind using this specific formula is to ensure that the ratio of the two tokens in the liquidity pool remains constant after the deposit. In Uniswap V2, liquidity pools operate based on the constant product invariant, which means that the product of the quantities of the two tokens in the pool remains constant. When users deposit tokens into the pool, they effectively change the ratio of the two tokens, and the minting function adjusts the amount of liquidity tokens minted to maintain this constant product. By using this formula, Uniswap V2 ensures that liquidity providers are fairly rewarded with liquidity tokens proportional to the liquidity they contribute to the pool while maintaining the constant product invariant necessary for the proper functioning of the AMM mechanism.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution  
    A sandwich attack is a form of front-running manipulation commonly seen in DEX and AMM like Uniswap. In a sandwich attack, a malicious actor exploits the transparency and predictability of on-chain transactions to profit at the expense of other traders. The attacker monitors the pending transactions in the pool of unconfirmed transactions of the blockchain network, looking for transactions that involve large trades or significant movements of assets. When the attacker identifies a large transaction about to be executed, they quickly submit their own transaction (usually with higher gas fees) to front-run the original transaction. This allows the attacker to manipulate the price in their favor before the original transaction is confirmed. After front-running the original transaction, the attacker executes a trade in the opposite direction, taking advantage of the manipulated price. The attacker profits from the price manipulation caused by their transactions, buying low and selling high (or vice versa) within a short timeframe. The original trader suffers from slippage, as the price they get for their trade is worse due to the manipulation.
