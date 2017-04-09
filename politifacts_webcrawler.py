import requests
from pyquery import PyQuery as pq

root = 'http://www.politifact.com/'
startPage = 'http://www.politifact.com/truth-o-meter/statements/?page=1'

def getSource(url):
	r = requests.get(url)
	return r.text

def getPages(url):
    results = []
    html = getSource(url)
    dom = pq(html)
    nextSelector = '.pagination .step-links__next'
    nextPage = dom(nextSelector)
    results.append(url)
    while nextPage:
            link = pq(nextPage[0]).attr('href')
            if link:
                nextPageLink = root + 'truth-o-meter/statements/' + link
                results.append(nextPageLink)
            else:
                break
            html = getSource(nextPageLink)
            #print(nextPageLink)
            dom = pq(html)
            nextPage = dom(nextSelector) 
    return results


#pages = getPages(startPage)
#print(pages)

#url = 'http://www.politifact.com/truth-o-meter/statements/?page=2'

def getStatementLinks(url):
    results = []
    html = getSource(url)
    dom = pq(html)

    links = dom('p.statement__text a[href]')

    for link in links:
        results.append(root + pq(link).attr('href'))
        #print(results)
    return results
#print(getStatementLinks(url))


#url = 'http://www.politifact.com//truth-o-meter/statements/2016/apr/11/tom-price/does-cbo-report-suggest-us-economy-faces-decade-pr/'
i=0
def getDetails(url):
    global i
    i = i+1
    Links = {}
    html = getSource(url)
    dom = pq(html)
    Links['Id'] = i
    Links['Sursa'] = dom('.statement__body p.statement__meta a[href]').text()
    Links['Text'] = dom('.statement__body div.statement__text').text()
    Links['ValoareDeAdevar'] = dom('.statement .meter img').attr('alt') 
    #print(Links)
    return Links

#stuff = getDetails(url)
#print(stuff)


details = []
def getAllStatements():
	pages = getPages(startPage)
	for p in pages:
		statementsLinks = getStatementLinks(p)
		for l in statementsLinks:
			details.append(getDetails(l))
	return details

# if __name__=='__main__':
#     statm = getAllStatements()
#     for s in statm:
#        print("am gasit: "+str(s))