import json
import urllib.request
import slackconf

def GetAccessToken(_code):
    url = 'https://slack.com/api/oauth.access?client_id={ClientID}&client_secret={ClientSecret}&code={Code}'.format(ClientID = slackconf.ClientID,ClientSecret = slackconf.ClientSecret,Code = _code)
    r = urllib.request.urlopen(url)
    root = json.loads(r.read().decode('utf-8'))
    #print(root)
    if root["ok"]:
        return root["access_token"],root["user"]
    else:
        return -1,""

def isInSpecificTeam(_token):
    url = 'https://slack.com/api/users.identity?token={token}'.format(token = _token)
    r = urllib.request.urlopen(url)
    root = json.loads(r.read().decode('utf-8'))
    #print(root)
    if root["ok"]:
        if root["team"]["id"] == slackconf.teamID:
            return True
    return False