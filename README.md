# Deep-Email
## A complete profile to an email using the Defastra API.

This script uses the Defastra Deep Email HLR Check API, aiming to be a tool in fraud prevention and osint research scenarios. The following data points are obtained: retrieves social media accounts linked to the email (Amazon, Nike, Foursquare, Facebook, Twitter, Atlassian, Badoo, Microsoft, Uber, Gravatar, Asus, Github, Indeed, Tumblr, Bitly, Myspace, Snapchat, Bukalapak, Kakaotalk, Vimeo, Tiktok, Yahoo, Patreon, Hubspot, Google and more...), validates availability, velocity, reputation, and scores risk, retrieves carrier, verify if its included in data breaches in json format.

## Prerequisites

To use this script, you'll need:

Python 3.x
A Deep Email Check API key from Defastra

## Installation

Clone this repository or copy the Deep-Email.py file to your local machine. Create a config.json file in the same directory as the script with your actual API key. See config.json for an example. Install the required Python packages by running pip3 install -r requirements.txt in the script's directory.

Usage

python3 Deep-Email.py -h                  

				                 ▄▄▄▄▄▄▄▄                                    
				         ▄▄██████████████████████▄▄                          
				    ▄▄███████▀▀▀            ▀▀▀▀███████▄                     
				 ▄█████▀▀                          ▀▀█████▄                  
			      ▄████▀▀                                   ▀████▄               
			    █████▀                                         ▀████             
			  ████▀                                              ▀████           
			▄███▀                                                  ▀████         
		       ████                                                      ▀███▄       
		     ▄███▀                                                         ███▄      
		    ▄███         ▀████████████████████████████████████████          ███▌     
		   ▐███         ▄  ▀▀██████████████████████████████████▀  ▄          ███▌    
		   ███▌         ████▄ ▀▀████████████████████████████▀  ▄███          ▐███    
		  ████          ███████▄  ▀██████████████████████▀  ▄██████           ████   
		  ███▀          ██████████▄  ▀████████████████▀  ▄█████████            ███   
		 ▐███           █████████████   ▀██████████▀   ████████████            ███▌  
		  ███           ██████████▀  ▄██▄  ▀████▀  ▄█▄  ▀██████████            ████  
		  ███           ███████▀  ▄████████▄    ▄███████▄      ▄▄              ████  
		 ▐███           ████▀  ▄████████████████████████  ▄█▀▀▀  ▀▀██▄         ███▌  
		  ███           █▀  ▄█████████████████████████▀ ▄█▀   ▄▄▄▄▄  ██        ███   
		  ███▌            ███████████████████████████▌ ██   ██▀▀▀██  ▐█▌      ▐███   
		  ▐███                                         ██  ██▀  ▐██  ▐█▀      ███▌   
		   ████                                        ██  ██▄▄▄██▌ ▄█▀      ████    
		    ████                                       ▀██  ▀▀▀   ▀▀▀       ████     
		     ████                                        ▀██▄    ▄▄        ████      
		      ▀███▄                                          ▀▀▀▀         ████       
		       ▀████                                                    ▄███▀        
			 ▀███▄                                                ▄████          
			   ▀████                                            ▄████            
			     ▀████▄                                      ▄████▀              
				▀█████▄                              ▄▄█████▀                
				   ▀██████▄▄                    ▄▄██████▀                    
				       ▀▀███████████▄▄▄▄████████████▀                        
				             ▀▀▀▀██████████▀▀▀▀                              
		=============================================================================
				          D E E P           E M A I L                        
		=============================================================================
				             author: Edgar Medina                            
		=============================================================================
		usage: Deep-Email.py [-h] email

		Check an email address with the Defastra API

		positional arguments:
		  email       the email address to check

		options:
		  -h, --help  show this help message and exit
      
      
## License
Author: Edgar Medina
This script is licensed under the MIT License.
