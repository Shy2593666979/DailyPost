import smtplib
from typing import Type
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from loguru import logger

from config import setting

class SendEmail:
    def __init__(self):
        self.sender = setting.EMAIL_SENDER
        self.receivers = setting.EMAIL_RECEIVERS
        self.email_type = setting.EMAIL_TYPE
        self.password = setting.EMAIL_PASSWORD

    def send_email(self, email_message, email_subject):
        if self.email_type.lower() == "qq":
            return self._email_qq(email_message, email_subject)
        if self.email_type.lower() == "163":
            return self._email_163(email_message, email_subject)
        if self.email_type.lower() == "gmail":
            return self._email_gmail(email_message, email_subject)

    def _email_qq(self, email_message, email_subject):
        return self._send(email_message, email_subject, "smtp.qq.com")

    def _email_163(self, email_message, email_subject):
        return self._send(email_message, email_subject, "smtp.163.com")

    def _email_gmail(self, email_message, email_subject):
        return self._send(email_message, email_subject, "smtp.gmail.com")

    def _send(self, email_message, email_subject, ssl_server):

        try:
            # 遍历所有收件人
            for receiver in self.receivers:
                # 帮助用户发送邮件，每次只发送一次
                server = smtplib.SMTP_SSL(ssl_server, 465)  # 发件人邮箱中的SMTP服务器，端口是465
                server.login(self.sender, self.password)  # 括号中对应的是发件人邮箱账号、邮箱密码

                # 构建邮件内容
                message = MIMEMultipart()

                message["From"] = Header('DailyPost <%s>' % self.sender)
                message["To"] = receiver
                message["Subject"] = email_subject

                body = email_message
                message.attach(MIMEText(body, "plain"))
                server.sendmail(self.sender, receiver, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件

                logger.info(f"sender: {self.sender}, receiver: {receiver}")
                server.quit()
        except Exception as err:
            logger.error(f"send email appear error : {err}")

emailer = SendEmail()