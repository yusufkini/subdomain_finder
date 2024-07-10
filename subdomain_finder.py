import requests

target_url = input("Enter your target (example: google.com) : ")
subdomain_list = []
url_control = []
controlled_url = ""

#Control for ".com" extension
for i in range(len(target_url)-1,len(target_url)-5,-1):
    url_control.append(target_url[i])
#Control for ".com" extension
for i in range(len(url_control)-1,-1,-1):
    controlled_url += url_control[i]

if controlled_url == ".com":
    wordlist = input("If you have any errors, specify the path of folder\nEnter your wordlist: ")
    try:
        with open(wordlist, mode="r") as f:
            lines = f.readlines()
            for line_index in lines:
                subdomain = line_index.strip()
                url = "https://" + subdomain + "." + target_url
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        subdomain_list.append(url)
                except:
                    pass
    except:
        print("Please enter your wordlist correctly! (or with .txt extension)")

    for subdomain in subdomain_list:
        print(subdomain)
else:
    print("Please enter your url as .com")