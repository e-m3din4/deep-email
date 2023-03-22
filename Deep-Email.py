import argparse
import json
import requests

# Banner
print("")
print("                                 ▄▄▄▄▄▄▄▄                                    ")
print("                         ▄▄██████████████████████▄▄                          ")
print("                    ▄▄███████▀▀▀            ▀▀▀▀███████▄                     ")
print("                 ▄█████▀▀                          ▀▀█████▄                  ")
print("              ▄████▀▀                                   ▀████▄               ")
print("            █████▀                                         ▀████             ")
print("          ████▀                                              ▀████           ")
print("        ▄███▀                                                  ▀████         ")
print("       ████                                                      ▀███▄       ")
print("     ▄███▀                                                         ███▄      ")
print("    ▄███         ▀████████████████████████████████████████          ███▌     ")
print("   ▐███         ▄  ▀▀██████████████████████████████████▀  ▄          ███▌    ")
print("   ███▌         ████▄ ▀▀████████████████████████████▀  ▄███          ▐███    ")
print("  ████          ███████▄  ▀██████████████████████▀  ▄██████           ████   ")
print("  ███▀          ██████████▄  ▀████████████████▀  ▄█████████            ███   ")
print(" ▐███           █████████████   ▀██████████▀   ████████████            ███▌  ")
print("  ███           ██████████▀  ▄██▄  ▀████▀  ▄█▄  ▀██████████            ████  ")
print("  ███           ███████▀  ▄████████▄    ▄███████▄      ▄▄              ████  ")
print(" ▐███           ████▀  ▄████████████████████████  ▄█▀▀▀  ▀▀██▄         ███▌  ")
print("  ███           █▀  ▄█████████████████████████▀ ▄█▀   ▄▄▄▄▄  ██        ███   ")
print("  ███▌            ███████████████████████████▌ ██   ██▀▀▀██  ▐█▌      ▐███   ")
print("  ▐███                                         ██  ██▀  ▐██  ▐█▀      ███▌   ")
print("   ████                                        ██  ██▄▄▄██▌ ▄█▀      ████    ")
print("    ████                                       ▀██  ▀▀▀   ▀▀▀       ████     ")
print("     ████                                        ▀██▄    ▄▄        ████      ")
print("      ▀███▄                                          ▀▀▀▀         ████       ")
print("       ▀████                                                    ▄███▀        ")
print("         ▀███▄                                                ▄████          ")
print("           ▀████                                            ▄████            ")
print("             ▀████▄                                      ▄████▀              ")
print("                ▀█████▄                              ▄▄█████▀                ")
print("                   ▀██████▄▄                    ▄▄██████▀                    ")
print("                       ▀▀███████████▄▄▄▄████████████▀                        ")
print("                             ▀▀▀▀██████████▀▀▀▀                              ")
print("=============================================================================")
print("                          D E E P           E M A I L                        ")
print("=============================================================================")
print("                             author: Edgar Medina                            ")
print("=============================================================================")

# Define the API endpoint URL
API_ENDPOINT = "https://api.defastra.com/deep_email_check"

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Check an email address with the Defastra API")
    parser.add_argument("email", help="the email address to check")
    args = parser.parse_args()

    # Retrieve API key from config file
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    api_key = config.get("api_key")

    # Set request headers and data
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "x-api-key": api_key,
    }
    data = {"email": args.email}

    # Send API request
    response = requests.post(API_ENDPOINT, data=data, headers=headers)

    # Print API response
    print(response.text)

if __name__ == "__main__":
    main()
