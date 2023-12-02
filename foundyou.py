import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def print_welcome():
    print(Fore.RED + """
                                          .-') _  _ .-') _                                        
                                         ( OO ) )( (  OO) )                                       
   ,------. .-'),-----.  ,--. ,--.   ,--./ ,--,'  \     .'_   ,--.   ,--..-'),-----.  ,--. ,--.   
('-| _.---'( OO'  .-.  ' |  | |  |   |   \ |  |\  ,`'--..._)   \  `.'  /( OO'  .-.  ' |  | |  |   
(OO|(_\    /   |  | |  | |  | | .-') |    \|  | ) |  |  \  ' .-')     / /   |  | |  | |  | | .-') 
/  |  '--. \_) |  |\|  | |  |_|( OO )|  .     |/  |  |   ' |(OO  \   /  \_) |  |\|  | |  |_|( OO )
\_)|  .--'   \ |  | |  | |  | | `-' /|  |\    |   |  |   / : |   /  /\_   \ |  | |  | |  | | `-' /
  \|  |_)     `'  '-'  '('  '-'(_.-' |  | \   |   |  '--'  / `-./  /.__)   `'  '-'  '('  '-'(_.-' 
   `--'         `-----'   `-----'    `--'  `--'   `-------'    `--'          `-----'   `-----'    
			
""" + Style.RESET_ALL)

def get_username():
    print(Fore.RED + "Enter the username to look up: ")
    username = input(Fore.WHITE + "@")
    return username

def crawl_web(username):
    websites = [
        "https://www.facebook.com/",
        "https://www.twitter.com/",
        "https://www.instagram.com/",
        "https://www.reddit.com/user/",
        "https://www.youtube.com/user/",
        "https://www.linkedin.com/in/",
        "https://www.pinterest.com/",
        "https://www.tumblr.com/blog/",
        "https://www.github.com/",
        "https://www.medium.com/@",
        "https://www.quora.com/profile/",
	"https://www.twitch.tv/",
	"https://www.spotify.com/user/",
    ]
    urls = []
    for website in websites:
        url = website + username
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            if soup.title and soup.title.string and username in soup.title.string:

                urls.append(url)
    return urls

def print_urls(urls):
    if not urls:
        print(Fore.RED + "No accounts were found with the username." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"{len(urls)} account(s) were found with the username." + Style.RESET_ALL)
        for url in urls:
            print(Fore.YELLOW + url + Style.RESET_ALL)


def main():
    print_welcome()
    username = get_username()
    urls = crawl_web(username)
    print_urls(urls)

main()
