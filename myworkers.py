# import subprocess


# import subprocess
# from sys import stderr, stdout

# api = str("D6106079-BBA2-06A96-93b5-BCe0cb1fa8f")

# # process = subprocess.Popen(['zoomeye' , 'init', '-apikey',api],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# process = subprocess.Popen(['zoomeye' , 'search','kstu.edu.gh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# out,err = process.communicate()
# if out:
#     print(out.decode())
# else:
#     print(err.decode())


# if target is None:
#     print(TRED + "Missing target! ==>",TWHITE + TGREEN + "Usage: crt.py -u target.com")
#     print("")
# else:
#     response = requests.get('https://crt.sh/?q=' + target + '&output=json')
#     json = response.json()
#     for show in json:
#         print(TGREEN + "[+] Found: ",TWHITE + show['common_name'])


"""
Sub-Domain discovery of domain
"""

import requests
import warnings

def subDomainSearch(url,filename,out=True):
    result = []
    filename = 'target-subdomain'
    warnings.filterwarnings("ignore")
    try:
        re = requests.get(url="https://crt.sh/?q=%s&output=json&exclude=expired" % url, verify=False).json()
        for i in re:
            result.append(i['name_value'])
        result = list(set(result))
        for i in result:
            print(i)
        if out != "-":
            with open(str(filename), mode='a') as filename:
                for i in result:
                    filename.write(str(i) + '\n')
    except Exception as e:
        print(e)

print(subDomainSearch('knust.edu.gh', 'newscan'))

# import requests, json

# class crtshAPI:
#     """crtshAPI main handler."""

#     def search(self, domain, wildcard=True, expired=True):
#         """
#         Search crt.sh for the given domain.
#         domain -- Domain to search for
#         wildcard -- Whether or not to prepend a wildcard to the domain
#                     (default: True)
#         expired -- Whether or not to include expired certificates
#                     (default: True)
#         Return a list of objects, like so:
#         {
#             "issuer_ca_id": 16418,
#             "issuer_name": "C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3",
#             "name_value": "hatch.uber.com",
#             "min_cert_id": 325717795,
#             "min_entry_timestamp": "2018-02-08T16:47:39.089",
#             "not_before": "2018-02-08T15:47:39"
#         }
#         """
#         base_url = "https://crt.sh/?q={}&output=json"
#         if not expired:
#             base_url = base_url + "&exclude=expired"
#         if wildcard and "%" not in domain:
#             domain = "%.{}".format(domain)
#         url = base_url.format(domain)

#         ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
#         req = requests.get(url, headers={'User-Agent': ua})

#         if req.ok:
#             try:
#                 content = req.content.decode('utf-8')
#                 data = json.loads(content)
#                 return data
#             except Exception as e: #ValueError
#                 print(e)
#                 data = json.loads("[{}]".format(content.replace('}{', '},{')))
#                 print(data)
#                 subList = []
#                 for sub in range(len(data)+1):
#                     subList.append(data['common_name'])
#                     print(data['name_value'])
#                 print(subList)
#                 # for i in subList:
#                 #     print('sub-domain discovered')
#                 #     print(i)
#             except Exception as err:
#                 print(err)
#         return None


# a = crtshAPI()
# print(a.search('knust.edu.gh'))