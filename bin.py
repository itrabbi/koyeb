import requests

def bin(bin, id, usertele):
    try:
        gbin = bin
        x1 = gbin[0]
        x2 = gbin[1]
        x3 = gbin[2]
        x4 = gbin[3]
        x5 = gbin[4]
        x6 = gbin[5]
        bin = x1 + x2 + x3 + x4 + x5 + x6
    except:
        pass
    try:
        gbin = bin.split("|")[0]
        x1 = gbin[0]
        x2 = gbin[1]
        x3 = gbin[2]
        x4 = gbin[3]
        x5 = gbin[4]
        x6 = gbin[5]
        bin = x1 + x2 + x3 + x4 + x5 + x6
    except:
        pass
    url = "https://data.handyapi.com/bin/" + bin
    r = requests.get(url).json()
    try:
        scheme = r.get('Scheme')
    except:
        scheme = "-----"
    try:
        type = r.get('Type')
    except:
        type = "-----"
    try:
        country = r.get('Country').get('Name')
    except:
        country = "-----"
    try:
        issuer = r.get('Issuer')
    except:
        issuer = "-----"
    
    
    tele = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ BIN Info</b>\n
<b>↯ Bin</b> ⌁ <code>{bin}</code>
<b>↯ Info</b> ⌁ <code>{scheme}-{type}</code>
<b>↯ Country</b> ⌁ <code>{country}</code>
<b>↯ Issuer</b> ⌁ <code>{issuer}</code>\n
↯ ReqBy ⌁ @{usertele} 
↯ DevBy ⌁ @rabbisudo
</strong>"""


    return tele


def bincc(bin, id, usertele):
    try:
        gbin = bin
        x1 = gbin[0]
        x2 = gbin[1]
        x3 = gbin[2]
        x4 = gbin[3]
        x5 = gbin[4]
        x6 = gbin[5]
        bin = x1 + x2 + x3 + x4 + x5 + x6
    except:
        pass
    try:
        gbin = bin.split("|")[0]
        x1 = gbin[0]
        x2 = gbin[1]
        x3 = gbin[2]
        x4 = gbin[3]
        x5 = gbin[4]
        x6 = gbin[5]
        bin = x1 + x2 + x3 + x4 + x5 + x6
    except:
        pass
    url = "https://data.handyapi.com/bin/" + bin
    r = requests.get(url).json()
    try:
        scheme = r.get('Scheme')
    except:
        scheme = "-----"
    try:
        type = r.get('Type')
    except:
        type = "-----"
    try:
        country = r.get('Country').get('Name')
    except:
        country = "-----"
    try:
        issuer = r.get('Issuer')
    except:
        issuer = "-----"
    
    tele = f"""<strong><b>↯ Bin</b> ⌁ <code>{bin}</code>
<b>↯ Info</b> ⌁ <code>{scheme}-{type}</code>
<b>↯ Country</b> ⌁ <code>{country}</code>
<b>↯ Issuer</b> ⌁ <code>{issuer}</code>\n
↯ ReqBy ⌁ @{usertele} 
↯ DevBy ⌁ @rabbisudo
</strong>"""
    return tele
