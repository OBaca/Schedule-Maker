from setuptools import setup
import sys

try:
    setup(
        app=["main.py"],
        options={
            "py2app": {
                "includes": ["openpyxl","customtkinter"],
                "resources": ["sheets/sheet.xlsx","manual/תבנית זמינות.xlsx","manual/תבנית סידור.xlsx","automate/תבנית זמינות.xlsx","automate/תבנית סידור.xlsx"]
            }
        },
        setup_requires=["py2app"],
    )
except Exception as e:
    print("An error occurred during setup for mac app.")
    print(e)
    sys.exit(1)