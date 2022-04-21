import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()

print(browser.open("http://support.worldpay.com/support/CNP-API/content/paytransrespcodes.htm"))
page = browser.page

# 
individual_row = page.find_all('tr', class_='TableStyle-StandardTable-Body-Normal')[0]
colunmns_by_row = individual_row.find_all('p')[0].text
print(colunmns_by_row)
