import base64


def pic2str(file, functionName):
    pic = open(file, 'rb')
    content = f'{functionName} = {base64.b64encode(pic.read())}\n'
    pic.close()
    # print(content)
    with open('picstr.py', 'a') as f:
        f.write(content)
def gitf2str(file):
    gifile = open(file, 'rb')
    content = f'gi = {gifile.read()}'
    gifile.close()
    with open('picstr.py', 'a') as f:
        f.write(content)

if __name__ == '__main__':
    pic2str('resource/queen.jpg', 'qq')
    pic2str('resource/spinning-arrows.gif','gg')
    gitf2str('resource/spinning-arrows.gif')