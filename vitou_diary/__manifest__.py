# -*- coding: utf-8 -*-
{
    'name': "Diary",
    'summary': "This module is diary for odoo17",
    'description': """
Long description of module's purpose
    """,
    'module_type': 'official',
    'author': "Mr. REAM Vitou, Tel: (+855) 17 82 66 82",
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
    'version': '17.0.1.0',
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

    'images': ['static/description/banner.gif'],
    "installable": True,
    "application": True,
    'license': 'LGPL-3',

}
