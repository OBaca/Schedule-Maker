from setuptools import setup
import sys

APP = ['main.py']
DATA_FILES = [
    ('sheets', ['sheets/sheet.xlsx']),
    ('manual', ['manual/תבנית זמינות.xlsx', 'manual/תבנית סידור.xlsx']),
    ('automate', ['automate/תבנית זמינות.xlsx', 'automate/תבנית סידור.xlsx']),
    ('Template', ['Template/תבנית זמינות.xlsx','Template/תבנית סידור.xlsx'])
]
OPTIONS = {
    'argv_emulation': True,
    'includes': ['openpyxl', 'customtkinter'],
    'plist': {
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleName': 'Shift-Schedule',
        'CFBundleIdentifier': 'com.obaca.Shift-Schedule',
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'Microsoft Excel Spreadsheet',
                'CFBundleTypeRole': 'Editor',
                'LSItemContentTypes': ['com.microsoft.excel.xls'],
                'LSHandlerRank': 'Alternate'
            }
        ]
    }
}

try:
    setup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )
except Exception as e:
    print("An error occurred during setup for macOS app.")
    print(e)
    sys.exit(1)