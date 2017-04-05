#!/usr/bin/env python

import sys
from mastodon import Mastodon

def td(x):
	if(type(x)==type([])):
		ret=""
		for item in x:
			ret+=td(item)
		return ret
	else:
		return "<td>"+x+"</td>"
def tr(x):
	if(type(x)==type([])):
		ret=""
		for item in x:
			ret+=tr(item)
		return ret
	else:
		return "<tr>"+x+"</tr>"
def br(x):
	if(type(x)==type([])):
		ret=""
		for item in x:
			ret+=br(item)
		return ret
	else:
		return x+"<br />"
def hr(x):
	if(type(x)==type([])):
		ret=""
		for item in x:
			ret+=hr(item)
		return ret
	else:
		return x+"<br /><hr />"
def link(url, x):
	return "<a href=\""+url+"\">"+x+"</a>"

def prettyPrintAcct(acct):
	print (td(link(acct["url"], br([
		"<b>"+acct["display_name"]+"</b>",
		"<i>"+acct["username"]+"</i>",
		"<img src=\""+acct["avatar"]+"\" width=\"100\" height=\"100\" />"
	]))))
def prettyPrintTootMedia(toot):
	if("media_attachments" in toot):
		print("<br />")
		if(toot["sensitive"]):
			print(hr(link(toot[url], "SENSITIVE MEDIA: CLICK TO VIEW")))
		else:
			for item in toot["media_attachments"]:
				print(link(item["url"], "<img src=\""+item["preview_url"]+"\" />"))
			print(hr(""))
def prettyPrintTootBody(toot):
	print("<td>")
	if(toot["spoiler_text"]):
		print(hr("CW: <b>"+toot["spoiler_text"]+"</b>"))
	else:
		print(hr(toot["content"]))
		prettyPrintTootMedia(toot)
	if(len(toot["tags"])>0):
		print(hr(" #".join(toot["tags"])))

	print("<a href=\""+toot["url"]+"\">permalink</a> ")
	print("("+str(toot["reblogs_count"])+" reblogs) ("+str(toot["favourites_count"])+" favs)")
	print("</td>")
def prettyPrintToot(toot):
	print("<tr>")
	prettyPrintAcct(toot["account"])
	prettyPrintTootBody(toot)
	print("</tr>")
def prettyPrintToots(toots):
	print("<table border=\"1\" style=\"width:100%; height:100%;\">")
	for toot in toots:
		prettyPrintToot(toot)
	print("</table>")

mastodon=Mastodon(sys.argv[1], access_token=sys.argv[2], api_base_url=sys.argv[3])
tl=mastodon.timeline_local()
print("<html><head><title>"+sys.argv[3]+" voyeur</title></head><body>")
print("<h1>"+link(sys.argv[3], sys.argv[3])+" voyeur</h1><br />")
prettyPrintToots(tl)
print("</body></html>")
