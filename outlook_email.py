import win32com.client

def send_email(str):
	olMailItem = 0x0
	obj = win32com.client.Dispatch("Outlook.Application")
	newMail = obj.CreateItem(olMailItem)
	newMail.Subject = str
	newMail.Body = "THE_BODY_HERE"
	newMail.To = "DESTINATION@EXAMPLE.COM"
	attachment1 = "c:\path\to\file.jpg"
	newMail.Attachments.Add(attachment1)
	newMail.Send()
	return
