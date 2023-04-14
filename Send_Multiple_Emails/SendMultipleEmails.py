import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo() #Identify yourself to an ESMTP server using EHLO
ob.starttls() #use Starttls protocol command
ob.login('photoan79@gmail.com', 'password')
subject="test python"
body="I LOVE Python"
massage="subject:{}\n\n{}".format(subject, body)
listadd=['photoan79@naver.com',
         "haokan617@naver.com"]
ob.sendmail('photoan79@gmail.com', listadd, massage)
print("send mail")
ob.quit()


