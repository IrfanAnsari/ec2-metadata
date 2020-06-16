#!/usr/bin/python
import urllib


def get(addr, api, uri):
    url = 'http://%s/%s/%s/' % (addr, api, uri)
    value = urllib.urlopen(url).read()
    print value
    if "404 - Not Found" in value:
        return None

    return value


def main():
    get('169.254.169.254','latest',"meta-data" )


if __name__ == "__main__":
    main()