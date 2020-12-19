#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1, 20)
    flowables = [report_title, empty_line]
    for text in paragraph:
        style = "Normal"
        if text == "\n":
            style = "BodyText"
        flowables.append(Paragraph(paragraph, styles[style]))
    report.build(flowables)