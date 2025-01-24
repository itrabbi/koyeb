import re
import requests
from cgen import cc_gen

def gg(m, id, user):

    cards = ""
    text = m
    bin_details = None

    if len(text) < 6:
        print("1",len(text))
        return f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ CC Generator</b>\n
↯ Invalid BIN\n
↯ ReqBy ⌁ @{id} 
↯ DevBy ⌁ @rabbisudo
</strong>"""
    
    input = re.findall(r"[0-9]+", text)
    
    if len(input) == 0:
        return f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ CC Generator</b>\n
↯ Invalid BIN\n
↯ ReqBy ⌁ @{id} 
↯ DevBy ⌁ @rabbisudo
</strong>"""
    
    if len(input) == 1:
        cc = input[0]
        mes = "x"
        ano = "x"
        cvv = "x"
    elif len(input[0]) < 6 or len(input[0]) > 16:
        return f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ CC Generator</b>\n
↯ Invalid BIN\n
↯ ReqBy ⌁ @{id} 
↯ DevBy ⌁ @rabbisudo
</strong>"""
    
    elif len(input) == 2:
        cc = input[0]
        mes = input[1]
        ano = "x"
        cvv = "x"
    elif len(input) == 3:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = "x"
    elif len(input) == 4:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]
    else:
        return f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ CC Generator</b>\n
↯ Invalid BIN
↯ Too many values provided.\n
↯ ReqBy ⌁ @{id} 
↯ DevBy ⌁ @rabbisudo
</strong>"""

    bin_api_url = f"https://data.handyapi.com/bin/{cc[:6]}" 
    
    try:
        response = requests.get(bin_api_url)
        bin_details = response.json()
        
        if bin_details['Status'] == "SUCCESS":
            scheme = bin_details.get('Scheme', '-----')
            card_type = bin_details.get('Type', '-----')
            country = bin_details['Country'].get('Name', '-----')
            issuer = bin_details.get('Issuer', '-----')
        else:
            scheme = card_type = country = "-----"
    except Exception as e:
        scheme = card_type = country = "Error fetching bin details"
    
    ccs = cc_gen(cc, mes, ano, cvv)
    cards = "\n".join(ccs)
    
    return f"""
    <strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ CC Generator</b>\n
<b>↯ Bin</b> ⌁ <code>{cc[:6]}</code> 
<b>↯ Info</b> ⌁ <code>{scheme}-{card_type}</code>
<b>↯ Country</b> ⌁ <code>{country}</code>
<b>↯ Issuer</b> ⌁ <code>{issuer}</code>\n
{cards} \n
↯ ReqBy ⌁ @{id} 
↯ DevBy ⌁ @rabbisudo</strong>
    """

   