# -*- coding: utf-8 -*-
{
    'name': "Diary",
    'author': 'REAM Vitou',
    'website': 'https://odoocambodia.com',
    'maintainer': 'REAM Vitou',
    'version': '18.0.0.1',
    'category': 'Human Resources',
    'sequence': 75,
    'summary': 'Staff Diary',
    'description': "Daily task and activity of staff or personal",
    'depends': [
        #'base'
        'mail',
        # 'hr.employee',
        'hr',
    ],
    'category': 'Human Resources',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/diary.xml',
        'views/status.xml',
        'views/priority.xml',
        'views/report_type.xml',
        'views/daily_report.xml',
        # 'data/sequence_diary.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'images': ['static/description/banner.gif'],
    "installable": True,
    "application": True,
    "auto_install": False,
    'license': 'LGPL-3',
}
