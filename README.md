

# Auto Crypto Sender

Auto Crypto Sender is a Python application used to automatically send cryptocurrency donations. This application interacts with the blockchain using the Web3 library and is specific to the BSC network.

## Installation

1. Make sure you have Python 3 installed to run the application.

2. Install the dependencies by running the following command:

   ```shell
   pip install web3 requests termcolor
   ```

3. Download the project files and navigate to the directory:

   ```shell
   git clone https://github.com/hydrokin/Auto-Crypto-Sender.git
   cd auto-crypto-sender
   ```

4. Edit the `network.txt` file and enter the network's RPC URL and chain ID:

   ```plaintext
   <rpc_url>
   <chain_id>
   ```

5. Edit the `bot.txt` file and enter the Telegram bot API key and chat ID:

   ```plaintext
   <api_key>
   <chat_id>
   ```

6. Start the Auto Crypto Sender application with the following command:

   ```shell
   python bot.py
   ```

## Usage

When you run Auto Crypto Sender, you can follow these steps:

1. First, it displays the donation message of Auto Crypto Sender, which includes the MATIC (Polygon) address.

2. Press "1" to display the menu options.

3. When you press "1", it prompts you to enter the receiver's address and the sender's private key. Enter these details correctly and press Enter.

4. Auto Crypto Sender displays the current block number, balance, gas limit, and total gas cost.

5. If the balance is greater than the total gas cost, the transaction is successfully executed, and a message is sent to the Telegram chat.

6. In case of errors, Auto Crypto Sender displays error messages and retries the transaction if necessary.

7. Close Auto Crypto Sender by pressing "2" in the menu.

## Notes

- Auto Crypto Sender uses the BSC network by default. If you want to use a different network, modify the RPC URL and chain ID in the `network.txt` file according to the desired network.

- Make sure to enter the Telegram bot API key and chat ID in the `bot.txt` file. Create a Telegram bot to obtain these credentials.

- Ensure that you provide accurate information such as the RPC URL, chain ID, API key, and chat ID for Auto Crypto Sender to function correctly.

This way, you can create a usage guide that will enable users to understand how to use Auto Crypto Sender. You can add or modify any additional details about the application as needed for user comprehension.
