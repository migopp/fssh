class Host:
    def __init__(self, data):
        self.host_name = data[0]
        self.status = data[1] == 'up'
        self.uptime = data[2][:len(data[2]) - 1] if ',' in data[2] else data[2]
        self.users = int(data[3]) if self.status else None
        self.load = float(data[4]) if self.status else None
        self.load_flag = data[5]

    def __str__(self):
        return f'[{self.host_name}, {self.status}, {self.uptime}, {self.users}, {self.load}, {self.load_flag}]'
