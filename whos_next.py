#!/usr/bin/python3
from time import sleep
import yaml
import random
import sys
import webbrowser
from dataclasses import dataclass

@dataclass
class StandupMember:
    name: str
    url: str

with open('members.yml','r') as m:
    member_yaml = yaml.safe_load(m)
    
members = list()
for member in member_yaml['standup_members']:
    members.append(StandupMember(member['name'],
                                 member['url']))


def generate_member():
    if not members:
        print("That's it! Everyone stood up, now go write code!")
        sys.exit(0)
    member = members.pop(random.randrange(len(members)))
    print(f"Go {member.name}!\n")
    webbrowser.open(member.url)    

from_console = "go"
while from_console != 'exit':
    from_console = input("\n\nGenerate a Standup Member manually,\nstart a countdown,\nor type exit to end (type countdown, exit, or press enter): ")
    if from_console == 'exit':
        sys.exit(0)
    if from_console == 'countdown':
        time = int(input('enter duration (in secords) for each standup: '))
        while True:
            generate_member()
            sleep(time)
    generate_member()



