import json
import urllib.request

# mobileNumber
# rollNo

def getID(mode, details):
    urlData = "http://admin.chotadhobi.com/college/58577760190a1f6a92174edb/students"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    all_students = json.loads(data.decode(encoding))["data"]

    for student in all_students:
        if str(student[mode]) == details:
            return student

