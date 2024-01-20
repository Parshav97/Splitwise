from services.ExpenseCreationService import ExpenseCreationService
from services.AbstractSubscriptionService import AbstractSubscriptionService
from model.UsersModel import UsersModel
import asyncio
import aiosmtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()

MAIL_PARAMS=os.getenv("MAIL_PARAMS")


class EmailService(AbstractSubscriptionService):
    user_model = None
    def __init__(self):
        ExpenseCreationService.subscription_services_list.append(self)
        self.user_model = UsersModel


    async def send_async_mail(self, sender, receivers, subject, texts, textType="plain"):
        
        msg = MIMEMultipart()
        msg.preamble = subject
        msg['Subject'] = subject
        msg['From'] = sender
        for i in range(0, len(receivers)):
            msg['To'] = receivers[i]
            msg.attach(MIMEText(texts[i], textType, 'utf-8'))
            smtp = aiosmtplib.SMTP(hostname=MAIL_PARAMS["host"], port=MAIL_PARAMS["port"], use_tls=MAIL_PARAMS["TLS"])
            await smtp.connect()
            await smtp.login(MAIL_PARAMS['user'], MAIL_PARAMS['password'])
            await smtp.send_message(msg)
            await smtp.quit()


        


    def on_expense_creation(self, args):

        expense = args[0]
        list_exp_trans = args[1]

        sender = self.user_model.query.filter(id=expense.paid_by)
        sender_email = sender["email_id"]

        receiver_mails = []
        receiver_msg = []
        for each in list_exp_trans:
            each_payer = self.user_model.query.filter(id=each.payer_id)
            each_mail = each_payer["email_id"]
            receiver_mails.append(each_mail)
            msg = "You have been added to an Expense by {}.\nThe total amount you owe for this expense is {}".format(sender_email, each["amount"])
            receiver_msg.append(msg)

        subject = "New Expense Is Created"



        mail = self.send_async_mail(sender_email, receiver_mails, subject, receiver_msg)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(mail))
        loop.close()



        
