from bs4 import BeautifulSoup
import requests
# with open('scraper/main.html', "r") as fileObj :
#     content = fileObj.read()
#     soup = BeautifulSoup(content, "lxml")  
#     tags = soup.find_all('h4')
#     for x in tags:
#         print(x.text)

# with open('scraper/main.html', "r") as fileObj :
#     content = fileObj.read()
#     soup = BeautifulSoup(content, "lxml")  
#     cards = soup.find_all('div', class_= "div1") 
#     for x in cards:
#         product = x.h4.text
#         price = x.button.text.split()[-1]
#         print(product + " cost " + price)

## SCRAPE A REAL WEBSITE
html_req = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=frontend+developer&txtLocation=')
req = html_req.text
soup = BeautifulSoup(req, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
# print(jobs)
info = []
for job in jobs:
    comp_name = job.find('h3', class_="joblist-comp-name")
    if comp_name.span:
        more = comp_name.find('span').clear()

    dated_posted = job.find('span', class_="sim-posted").span.text
    companyName =comp_name.text.lower()
    Skills = job.find('span', class_='srp-skills').text.replace(" ", '')
    jobdata = {
        "name" : companyName,
        "skill" : Skills,
        "dateposted" : dated_posted
    }
    info.append(jobdata)
# print(info)
with open('scraper/user.html', 'w') as scraped_data:
     for x in info:   
        # print(x['name'])     
        scraped_data.write(
            f"""
                <div>
                <hr>
                    <ul type = "none">
                        <li><h3>{x['name']}</h3></li>
                        <li><strong>Skills required :</strong> {x['skill']}</li>
                        <li><strong>date posted :</strong> {x['dateposted']}</li>
                    </ul>
                    <hr>
                </div
            """
        )
    
            
    # print(f"""
    # company :{companyName} 
    # required Skills: {Skills}
    # date posted : {dated_posted}
    # """)