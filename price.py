def shopping(shop_file):
    global shop_dict
    shop_dict = {} # 생성할 사전 객체
    file='data/'+str(shop_file)

    myWget=open(file, 'r')
    lines=myWget.read()
    lines=lines.replace('원', '')
    myWget.close()
    myWget=open(file, 'w')
    myWget.write(lines)
    myWget.close

    with open(file, 'r') as myWget:
        value=0
        lines=myWget.read()
        s=lines.split()
        del s[0]
        del s[0]
        for line in s:
            try:
                value=int(line)
            except:
                key=line
            shop_dict[key]=value

        return shop_dict


def item_price(shop_file, item):
    shopping(shop_file)

    return shop_dict.get(item)