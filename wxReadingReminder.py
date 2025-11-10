# -*- coding: utf-8 -*-
# @Time : 2024/1/24
# @Author : 52595
# @File : wxReadingReminder.py
# @Python Version : 3.7.4
# @Software: PyCharm

import re
import json
from prettytable import PrettyTable
import pandas as pd
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 邮件配置
EMAIL_CONFIG = {
    'smtp_server': os.getenv('SMTP_SERVER', 'smtp.qq.com'),
    'smtp_port': int(os.getenv('SMTP_PORT', 587)),
    'sender_email': os.getenv('SENDER_EMAIL'),
    'sender_password': os.getenv('SENDER_PASSWORD'),
    'receiver_email': os.getenv('RECEIVER_EMAIL')
}


def send_email(subject, content):
    """发送邮件通知"""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_CONFIG['sender_email']
    msg['To'] = EMAIL_CONFIG['receiver_email']
    msg['Subject'] = subject

    msg.attach(MIMEText(content, 'html'))

    try:
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        print(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.send_message(msg)
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")

def main():
    # 邮件内容
    html_content = f"""
    <h2>记得在微信读书读会书，别中途了</h2>
    """
    
    # 发送邮件
    # 设置邮件标题
    subject = f"微信读书365日挑战"
    send_email(subject, html_content)

if __name__ == "__main__":
    main()
