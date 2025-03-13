# -*- coding: utf-8 -*-
{
    'name': "Diary",
    'summary': "Staff diary is for recording ever staff by themself for daily tasks and activity",
    'description': """
        This module is for daily staff diary.
    """,
    'module_type': 'official',
    'maintainer': 'Vitou Technologies',
    'author': "Vitou Technologies",
    'version': '17.0.1.0',
    'website': "https://www.odoocambodia.com",
    'depends': [
        #'base',
        'base_setup',
        'mail',
        # 'hr.employee',
        #module name
        'hr',
    ],
    'category': 'Human Resources',
    # any module necessary for this one to work correctly

    # always loaded
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

    'images': ['static/description/banner.png'],
    "installable": True,
    "application": True,
    'license': 'LGPL-3',

}
