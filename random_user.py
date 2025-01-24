import requests


def geninfo(id, usertele,country_code,admin_username):
    u = f"https://randomuser.me/api/1.4/?nat={country_code}"
    r = requests.get(u).json()
    rs = r["results"][0]
    gender = rs["gender"]
    title = rs["name"]["title"]
    first = rs["name"]["first"]
    last = rs["name"]["last"]
    lo = rs["location"]
    streetnumber = lo["street"]["number"]
    streetname = lo["street"]["name"]
    city = lo["city"]
    state = lo["state"]
    country = lo["country"]
    postcode = lo["postcode"]
    offset = lo["timezone"]["offset"]
    description = lo["timezone"]["description"]
    email = rs["email"]
    login = rs["login"]
    uuid = login["uuid"]
    username = login["username"]
    password = login["password"]
    salt = login["salt"]
    dob = rs["dob"]
    date = dob["date"]
    age = dob["age"]
    phone = rs["phone"]
    cell = rs["cell"]
    idname = rs["id"]["name"]
    image = rs["picture"]["large"]
    return f"""
<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Address Generator</b>\n
↯ Name ⌁ <code>{first} {last}</code>
↯ ZIP ⌁ <code>{postcode}</code>
↯ City  ⌁ <code>{city}</code>
↯ State ⌁ <code>{state}</code>
↯ Address ⌁ <code>{streetnumber} {streetname}</code>
↯ Country ⌁ <code>{country}</code>\n
↯ Country Code ⌁ <code>AU, BR, CA, CH, DE, DK, ES, FI, FR, GB, IE, IN, IR, MX, NL, NO, NZ, RS, TR, UA, US</code>\n
↯ ReqBy ⌁ @{usertele} 
↯ DevBy ⌁ {admin_username}</strong>"""
