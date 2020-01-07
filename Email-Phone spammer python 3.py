import smtplib, time, random

# I am not responsible for anything you do using this. Use at your own risk and only use it for """"testing"""" purposes >:)
# if you want to take this one step further you can sign them up for alerts and random crap online using their phone
# number email. but again: I accept no responsibility ;)


gmail = 'USERNAME@gmail.com'
passwd = 'PASSWORD'

# amount of messages to send
num_times = 100

# If you're using this to spam a phone number then you must know what carrier they use. A few ways to find out:
# 1. Ask them lol
# 2. Use an online service such as fonefinder.net (note that this isn't always accurate and didn't tell me the correct one for my number)
# 3. Send a mail using each domain. If the carrier is incorrect you will receive an email back saying that the number can't be found


# AT&T number@txt.att.net
# Verizon number@vtext.com
# T-Mobile number@tmomail.net
# Sprint number@messaging.sprintpcs.com or number@pm.sprint.com
# Virgin Mobile number@vmobl.com
# Nextel number@ messaging.nextel.com
# Alltel number@messaging.alltel.com
# Metro PCS number@mymetropcs.com
# Powertel number@ptel.com
# Boost Mobile number@myboostmobile.com
# Suncom number@tms.suncom.com
# Tracfone number@mmst5.tracfone.com
# U.S. Cellular number@email.uscc.net
# Qwest number@qwestmp.com

# example: A sprint number of (123) 456-7890 would be 1234567890@pm.sprint.com

# the email or email phone number to spam
to = ['1234567890@pm.sprint.com']

# the subject of the mail
subj = 'Subject'


try:
    # if you wanna use another service change the smtp and port here
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail, passwd)

    for i in range(num_times):
        # if you don't want a random message just change 'body' to a constant string value like 'body = "test"'
        body = ''.join(random.choice('!@#$%^&*()-=_+[]{};",.<>/?`~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')\
                       for x in range(random.randint(10,30)))


        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (gmail, ", ".join(to), subj, body)


        server.sendmail(gmail, to, email_text)
        time.sleep(1)
        print('message ', i, ' sent')

    server.close()
    print('Finished')
except Exception as e:
    print(e)
    print('Failed')

    # if you get
    # (535, b'5.7.8 Username and Password not accepted...') or something of similar not being able to log in then
    # your username or password is either wrong or you must enable 'Less secure app access' under
    # https://myaccount.google.com/u/1/lesssecureapps
    # Note: this won't work on accounts with 2FA. best to use a throw away account as the receiver will also be
    # able to see the email you send with