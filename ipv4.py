import subprocess
import time
from lcd_lib import setText, setRGB

ipv4 = ''

while len(ipv4) == 0:

    result = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)

    ipv4 = result.stdout.decode('utf-8').split(' ')[0]

    time.sleep(10)

setRGB(0, 128, 0)
setText(f'IPv4: {ipv4}')