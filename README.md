# Auto-Crypto-Sender-For-BSC

Auto Crypto Sender like Sweeper Bot

How to use ;


1. Install the required libraries:
   - `web3`: Used for interacting with Binance Smart Chain.
   - `termcolor`: Used for providing colored outputs in the printed text.

   You can install these libraries using the pip package manager with the following commands:
   ```
   pip install web3
   pip install termcolor
   ```

2. Copy the code into a Python file (e.g., `crypto_bot.py`).

3. Run the file in a Python environment such as Jupyter Notebook, Visual Studio Code, or a terminal:
   ```
   python bot.py
   ```

4. When the program starts, it will begin listening to new blocks and prompt you for some inputs. You need to provide these inputs correctly:
   - `Enter the receiver's address`: Enter the address of the account to which the crypto will be sent.
   - `Enter the sender private key`: Enter the private key of the account sending the crypto.

5. The bot will listen to new blocks and attempt to make a crypto transfer by checking your balance. Output messages will be printed to monitor the bot's status.

   - `Listening to new block`: Indicates the bot is listening to new blocks.
   - `========== Auto Crypto Sender Status ==========`: A header showing the status of the bot.
   - `Latest Block Number`: The latest block number.
   - `Balance`: The balance in the account.
   - `Gas Limit`: The gas limit set for the transfer transaction.
   - `Total Gas Cost`: The total gas cost of the transfer transaction.
   - `Sending Successful!`: Indicates a successful transfer.
   - `Success! Transferred --> {amount}`: Displays the transferred amount.
   - `Transaction confirmed!`: The transaction has been successfully confirmed.
   - `Transaction failed! Retrying with a new nonce.`: The transaction failed, and the bot will retry with a new nonce value.
   - `Error: {error_msg}`: Displays error messages.

6. To terminate the program, press `Ctrl+C` in the running Python environment.

Please be cautious as this code can perform real crypto transfers and may result in crypto loss if used incorrectly. It is recommended to test the code on a Binance Smart Chain test network or with small amounts of crypto before using real keys and large amounts of crypto. Make sure to review the code carefully.
