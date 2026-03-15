from tools.apollo_tool import search_founders
from agents.research_agent import summarize_company
from agents.outreach_agent import generate_email

query = input("Search founders: ")

results = search_founders(query)

for person in results["people"][:5]:

    name = person["name"]
    company = person["organization"]["name"]

    summary = summarize_company(company)

    email = generate_email(name, company)

    print("Founder:", name)
    print("Company:", company)
    print("Summary:", summary)
    print("Cold Email:", email)
    print("--------------------")