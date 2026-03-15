# AI Founder Research Agent

An AI-powered automation system that discovers startup founders, researches their companies, and generates personalized outreach emails automatically.

This project demonstrates how AI agents + APIs + automation workflows can reduce hours of manual lead research into a few seconds.

It is designed as a prototype for AI-driven sales research and founder discovery tools.

---

## Problem

Startup founders, sales teams, and investors spend a lot of time:

- Searching for relevant founders
- Researching companies
- Understanding their products
- Writing personalized outreach emails

This process is manual, repetitive, and time-consuming.

---

## Solution

AI Founder Research Agent automates the workflow:

1. Find founders using lead generation APIs
2. Research their company information
3. Summarize the startup using AI
4. Generate a personalized outreach email

This demonstrates how AI agents can automate founder research pipelines.

---

## Features

- Founder discovery using Apollo API
- LinkedIn profile enrichment
- AI-powered startup research
- Automatic company summaries
- Personalized cold email generation
- Modular AI agent architecture

---

## Project Architecture

User Query  
↓  
Founder Search Agent  
↓  
Data Enrichment (Apollo + LinkedIn)  
↓  
Research Agent (Startup Summary)  
↓  
Outreach Agent (Email Generation)  
↓  
Structured Output

---

## Tech Stack

- Python
- LangChain
- Large Language Models
- Apollo API
- BeautifulSoup
- Requests

---

## Environment Setup

Create a `.env` file in the root folder:

OPENAI_API_KEY=your_openai_key  
APOLLO_API_KEY=your_apollo_key

---

## Running the Project

Run the main script:

python main.py

Example input:

Search founders: AI SaaS founders in India

The agent will:

- Fetch founders
- Summarize companies
- Generate personalized outreach emails

---

## Example Output

Founder: Rahul Sharma  
Company: AIStack  

Summary:  
AIStack builds AI-powered automation tools for small businesses.

Generated Email:

Hi Rahul,

I came across AIStack and really liked how you're helping small businesses automate workflows with AI.

I'm currently building AI research agents and would love to learn more about your journey.

---

## Future Improvements

- Web dashboard interface
- CRM integrations
- Autonomous multi-agent workflows
- Better founder enrichment
- Lead scoring using AI
- Integration with more data providers

---

## Use Cases

- Startup lead generation
- Founder research automation
- Sales prospecting
- VC deal sourcing
- AI automation experiments


## Author

Manas Khatri  
Mathematics & Computing Student  
Exploring AI agents, automation systems, and startup tooling

---

## Contributing

Pull requests and ideas are welcome.  
If you have suggestions for improving the agent workflow or adding new integrations, feel free to open an issue.
