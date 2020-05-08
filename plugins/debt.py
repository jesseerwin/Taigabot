from util import hook, request
from bs4 import BeautifulSoup


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    query = soup.find(id='debtDisplay')
    
    if query is None:
        return "unknown"
    else:
        return "$" + query.get_text()


@hook.command(autohelp=False)
def debt(inp):
    """debt -- returns the us national debt"""

    url = "https://commodity.com/debt-clock/us/"
    html = request.get_html(url)
    debt = parse(html)

    return "Current US Debt: \x02{}\x02".format(debt)
