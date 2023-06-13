from web3 import Web3
import requests
from termcolor import colored


def read_network_info():
    try:
        with open("network.txt", "r") as file:
            lines = file.readlines()
            rpc_url = lines[0].strip()
            chain_id = int(lines[1].strip())
            return rpc_url, chain_id
    except FileNotFoundError:
        print(colored("Error: Network file 'network.txt' not found.", "red"))
        exit(1)


def read_bot_info():
    try:
        with open("bot.txt", "r") as file:
            lines = file.readlines()
            api_key = lines[0].strip()
            chat_id = lines[1].strip()
            return api_key, chat_id
    except FileNotFoundError:
        print(colored("Error: Bot file 'bot.txt' not found.", "red"))
        exit(1)


def print_donation_message():
    message = "Thank you for choosing Auto Crypto Sender!\n" \
              "You can use this tool to send cryptocurrency donations.\n" \
              "My polygon address for donation: 0xface84CB2B2f4baB7A5e130d39C36C7e1b679331"
    print(colored(message, "green"))


def print_menu():
    print("================== Auto Crypto Sender ==================")
    print("1. Send Transaction")
    print("2. Exit")
    print("=======================================================")


def print_bot_status(block_number, balance, gas_limit, total_gas_cost):
    message = f"========== Auto Crypto Sender Status ==========\n" \
              f"Latest Block Number: {block_number}\n" \
              f"Balance: {balance} ETH\n" \
              f"Gas Limit: {gas_limit}\n" \
              f"Total Gas Cost: {total_gas_cost} ETH\n" \
              f"==============================================="
    print(colored(message, "cyan"))


def already_known_error():
    message = "gas fee paid"
    print(colored(f"Error: {message}", "yellow"))


def send_telegram_message(api_key, chat_id, message):
    url = f"https://api.telegram.org/bot{api_key}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "disable_web_page_preview": True
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(colored("Failed to send Telegram message.", "red"))


def bot():
    rpc_url, chain_id = read_network_info()
    provider = Web3.HTTPProvider(rpc_url)
    web3 = Web3(provider)

    api_key, chat_id = read_bot_info()

    print_donation_message()

    print('Listening to new block')

    while True:
        try:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                send_transaction(web3, chain_id, api_key, chat_id)
            elif choice == "2":
                break
            else:
                print(colored("Invalid choice. Please try again.", "red"))

        except KeyboardInterrupt:
            
            break

        except Exception as e:
            print(f"Error: {e}")


def send_transaction(web3, chain_id, api_key, chat_id):
    address_receiver = input("Enter the receiver's address: ")
    private_key = input("Enter the sender private key: ")

    account = web3.eth.account.from_key(private_key)

    while True:
        try:
            latest_block = web3.eth.block_number
            balance = web3.eth.get_balance(account.address)
            gas_limit = web3.eth.estimate_gas({
                'to': address_receiver,
                'value': balance
            })
            gas_price = web3.eth.gas_price
            gas1 = gas_limit * 5
            gas2 = gas1 // 3
            total_gas_cost = gas2 * gas_price

            print_bot_status(latest_block, balance, gas_limit, total_gas_cost)

            if balance - total_gas_cost > 0:
                print(colored("Sending Successful!", "green"))
                amount_eth = (balance - total_gas_cost) / 10**18

                try:
                    nonce = web3.eth.get_transaction_count(account.address)

                    while True:
                        transaction = {
                            'to': address_receiver,
                            'value': balance - total_gas_cost,
                            'gas': gas_limit,
                            'gasPrice': gas_price,
                            'nonce': nonce,
                            'chainId': chain_id
                        }

                        signed_tx = account.sign_transaction(transaction)
                        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
                        print("Success! Transferred --> gas fee paid")

                        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
                        if receipt.status:
                            message = f"Transaction confirmed! Amount: {amount_eth} ETH"
                            send_telegram_message(api_key, chat_id, message)
                            break
                        else:
                            print("Transaction failed! Retrying with a new nonce.")
                            nonce += 1 

                except Exception as e:
                    error_msg = str(e)
                    if error_msg == "{'code': -32000, 'message': 'already known'}":
                        already_known_error()
                    elif error_msg == "{'code': -32000, 'message': 'replacement transaction underpriced'}":
                        already_known_error()
                    else:
                        print(f"Error: {e}")

        except KeyboardInterrupt:
            
            break

        except Exception as e:
            print(f"Error: {e}")

        latest_block += 1


bot()
