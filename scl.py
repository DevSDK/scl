import json
from os import path
from notion.client import NotionClient
from notion.block import PageBlock, TextBlock, DividerBlock, TodoBlock

if not path.exists('config.json'):
    data = {}
    data["Auth"] = ""
    data["Page"] = ""
    with open('config.json', 'w+') as outfile:
        json.dump(data, outfile)

def AskInformation():
    print('Type (defualt: commit): ', end="")
    target = input()
    if(len(target) == 0):
        target="commit"
    print('Title: ', end="")
    title = input()
    if(len(title) == 0):
        title = "Untitled"
    print('URL or additional information (Not required): ', end="")
    info = input()
    if(len(info) == 0):
        info = "N/A"

    return title, info, target

def CreateCheckList(page):
    title, info, target = AskInformation()
    case = page.children.add_new(PageBlock)
    case.title = title
    infoblock = case.children.add_new(TextBlock)
    infoblock.title="Addition Information: " + info
    case.children.add_new(DividerBlock)
    with open('checklist.json') as json_file:
        data = json.load(json_file)
        for todo_title in data[target]:
             todo = case.children.add_new(TodoBlock)
             todo.title = todo_title

    return

with open('config.json') as json_file:
    data = json.load(json_file)
    client = NotionClient(token_v2=data["Auth"])
    page = client.get_block(data["Page"])
    CreateCheckList(page)
    

