#!/usr/bin/env
import subprocess, time, re

# regex patterns to match time. HH:MM:SS
prompts = {
    '08:30:00':'Stop what you are doing and get started.',
    '11:00:00':'Lunch!',
    '12:30:00':'Lunch is over, get started.',
    '13:00:00':'',
    '13:30:00':'',
    '17:30:00':'',
    '..:.1:00': 'focus',
    '..:.6:00': 'focus',
    '..:00:00': 'Begin work cycle',
    '..:55:00': 'End work cycle. 5 minute break',
}

SAYCMD = '/usr/bin/say'
def say(s):
    subprocess.call([SAYCMD, s])

def get_time():
    return(time.strftime("%H:%M:%S"))

if __name__ == "__main__":
    while True:
        t = get_time()
        for prompt in prompts.keys():
            if re.match(prompt, t):
                say(prompts[prompt])

        time.sleep(0.6)
