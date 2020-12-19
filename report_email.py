#!/usr/bin/env python3
import os
import datetime

import reports
import emails

if __name__ == '__main__':
    DESC_DIR = os.path.join(os.path.expanduser("~"), 'supplier-data', 'descriptions')
    attachment = "processed.pdf"
    today = datetime.datetime.now().strftime("%B %d, %Y")
    title = f"Processed Update on {today}"

    paragraphs = []
    for file in os.listdir(DESC_DIR):
        with open(os.path.join(DESC_DIR, file)) as f:
            name, weight, _ = f.readlines()
            paragraphs.append(f"name: {name}weight: {weight}")

    reports.generate_report(attachment, title, "\n".join(paragraphs))
    emails.generate_email(
        sender="automation@example.com",
        recipient="username@example.com",
        subject="Upload Completed - Online Fruit Store",
        body="All fruits are uploaded to our website successfully. A detailed list is attach to this email",
        attachment=attachment)