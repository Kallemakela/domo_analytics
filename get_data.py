from robobrowser import RoboBrowser
import config

def get_data():
    url = 'https://domo.ayy.fi/customers/sign_in'
    br = RoboBrowser()
    br.open(url)
    form = br.get_form()
    form['customer[email]'].value = config.email
    form['customer[password]'].value = config.password
    br.submit_form(form)
    data = br.find_all("li")
    #remove 2 first li elements
    return data[2:]
