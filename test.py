# coding:utf-8
import requests
import json
import datetime

dt = datetime.datetime.now() - datetime.timedelta(days=1)
issues_url = "https://api.github.com/repos/kamonohashiK/blog_automation/issues?direction=asc&since={}"
issues = issues_url.format(dt.date())

response = requests.get(issues)
res = response.json()

for r in res:
    title = r['title']
    print(title)

    number = str(r['number'])
    comments_url = "https://api.github.com/repos/kamonohashiK/blog_automation/issues/{}/comments"
    response = requests.get(comments_url.format(number))

    comments = response.json()
    for c in comments:
        print(c['body'] + "\n")
