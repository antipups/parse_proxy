import re
import requests


def parse_proxy():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
               'cookie':'cookie: __cfduid=df1d41775d59c3fe8f36e04fcca378a341581148925; t=157298446; PAPVisitorId=8dcaadea3a7fe7e021577e7086bbzMiC; PAPVisitorId=8dcaadea3a7fe7e021577e7086bbzMiC; _ga=GA1.2.996540714.1581148926; _gid=GA1.2.89029046.1581148926; _ym_uid=1581148926995199122; _ym_d=1581148926; _ym_wasSynced=%7B%22time%22%3A1581148925963%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; jv_enter_ts_PeHzjrJoSL=1581148926353; jv_visits_count_PeHzjrJoSL=1; _fbp=fb.1.1581148926486.29804592; _ym_isad=2; cf_clearance=3fa1b6e40887093916981b7597d7e199c2a73e4e-1581152615-0-150; a_uid=710c764c0fd804b2863fd415984e1af4%7C5e3e7a5c; _ym_visorc_42065329=w; jv_invitation_time_PeHzjrJoSL=1581172521358; jv_close_time_PeHzjrJoSL=1581172531959; jv_pages_count_PeHzjrJoSL=7'
               }
    html = requests.get('https://hidemy.name/ru/proxy-list/?__cf_chl_jschl_tk__=a53058d263a7a6f0b21858fc818edfff8869b715-1581152611-0-ATXSvJTXPNT32xhQB_FGkW80AgoAAh8XXAFAVVcOy11dGlUkR5e4JaFwtLcoAP7u4tQ6Si9Cwe_eRdOITKeDZEUVuVcasq9MNhEQVQSKSwZhkqpfUtD2s2nz7gKIaGIkhbwErB0D9_N0FIdzWEMQX2meWV0Rhf1TQhxvBYiq0uj7W-QTmCtNLKVZFMljs281ntusj4vn55ERr4lFBsGhpklPzfV68ij64HO9IPV6Dq6ryo2DYdGSBmGsYqR0u-igN9nNZ9VwuROuaEozB9b5MWnfBASGt0raW8_XbbKABzmI',
                        headers=headers).text
    all_urls = re.findall(r'<tr><td>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}<\/td><td>\d{1,6}<\/td>', html)
    return tuple(map(lambda x: re.sub('</td><td>', ':', x)[8:-5], all_urls))


if __name__ == '__main__':
    print(parse_proxy())

