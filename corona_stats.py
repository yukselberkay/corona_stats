import argparse
import requests

def argument_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=function_map.keys())
    args = parser.parse_args()
    func = function_map[args.command]
    func()
    
def get_all_stats():
    url = "https://corona.lmao.ninja/all"
    response = requests.get(url)
    content = response.json()
    for key,value in content.items():
        print(key + " => " + str(value))


def get_by_country():
    ct_name = input("Enter Country Name : ")
    ct_name = ct_name.lower()
    url = "https://corona.lmao.ninja/countries/%s" % ct_name
    response = requests.get(url)
    content = response.json()
    for key,value in content.items():
        print(key + " => " + str(value))

function_map = {'all' : get_all_stats,'country' : get_by_country}
argument_parse()