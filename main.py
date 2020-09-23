# coding:utf-8
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json
import datetime

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GITHUB_ID = os.environ.get("GITHUB_ID")
REPOSITORY_NAME = os.environ.get("REPOSITORY_NAME")
HATENA_ID = os.environ.get("HATENA_ID")
BLOG_URL = os.environ.get("BLOG_URL")
HATENA_PASSWORD = os.environ.get("HATENA_PASSWORD")

def fetchGithub():
	dt = datetime.datetime.now() + datetime.timedelta(hours=9)
	issues_url = "https://api.github.com/repos/{}/{}/issues?direction=asc&state=all&since={}T00:00:0Z"
	issues = issues_url.format(GITHUB_ID, REPOSITORY_NAME, dt.date())

	response = requests.get(issues)
	res = response.json()

	blog_title = "Issueなし"
	blog_body = "無為に過ごした1日"

	if len(res) != 0:
		blog_title = res[0]['title']
		blog_body = ""

		for r in res:
			headline = "### " + r['title'] + "\n"
			blog_body += headline
			blog_body += r['body'] + "\n\n"

			number = str(r['number'])
			comments_url = "https://api.github.com/repos/{}/{}/issues/{}/comments"
			response = requests.get(comments_url.format(GITHUB_ID, REPOSITORY_NAME, number))

			comments = response.json()
			for c in comments:
				blog_body += c['body'] + "\n\n"

	#postHatena(blog_title, blog_body)

def postHatena(title, body):
	date = datetime.datetime.now()
	xml_template = """<?xml version="1.0" encoding="utf-8"?>
	<entry xmlns="http://www.w3.org/2005/Atom"
		xmlns:app="http://www.w3.org/2007/app">
	<title>{}</title>
	<author><name>virtual-surfer</name></author>
	<content type="text/x-markdown">{}
	</content>
	<updated>{}</updated>
	<category term="自動投稿" />
	<app:control>
		<app:draft>yes</app:draft>
	</app:control>
	</entry>
	""".format(title, body, date)

	headers = { "Content-type": "application/xml" }

	hatena_url = "https://blog.hatena.ne.jp/{}/{}/atom/entry"
	request = requests.post(
		hatena_url.format(HATENA_ID, BLOG_URL), timeout=10, headers=headers, data=xml_template.encode("utf-8"),
		auth=HTTPBasicAuth(HATENA_ID, HATENA_PASSWORD)
	)

	print(request)

def main():
    fetchGithub()

if __name__ == "__main__":
    main()