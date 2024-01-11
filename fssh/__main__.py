import os
import requests
import subprocess
from bs4 import BeautifulSoup
from host import Host

SSH_LOGIN_TEMPLATE = 'ssh {}@{}.cs.utexas.edu'
USER = 'UTCS_USERNAME'
PASS = 'UTCS_PASSPHRASE'

def fssh():
    hosts = filter_hosts(get_hosts())
    if not hosts:
        print('ERR: NO HOSTS AVAILABLE')
        return;

    command = SSH_LOGIN_TEMPLATE.format(os.environ[USER], hosts[len(hosts) - 1].host_name)
    os.system(command)

def get_hosts():
    hosts_page = requests.get('https://apps.cs.utexas.edu/unixlabstatus/')
    soup = BeautifulSoup(hosts_page.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')[3:]

    hosts = []
    for row in rows:
        cols = row.find_all('td')
        load_flag = 'background-color: yellow' in cols[0]['style']
        cols = [col.text.strip() for col in cols]
        cols.append(load_flag)
        hosts.append(Host(cols))

    return hosts

def filter_hosts(hosts):
    # filter status
    hosts = list(filter(lambda host: host.status, hosts))

    # filter high average load
    temp_hosts = list(filter(lambda host: not host.load_flag, hosts))
    hosts = temp_hosts if len(temp_hosts) > 0 else hosts

    # min load
    min_load = min(host.load for host in hosts)
    hosts = list(filter(lambda host: host.load == min_load, hosts))

    # min users
    min_users = min(host.users for host in hosts)
    hosts = list(filter(lambda host: host.users == min_users, hosts))

    return hosts

if __name__ == '__main__':
    fssh()
