# -*- coding: utf-8 -*-
{
    'name': "Neuron",

    'summary': "Interactive Phone Script Assistant",

    'description': """
        The script assistant is a universal tool in which you can program all the options for developing a conversation for your managers.
        A tool that leads the manager automatically to a deal with a client.
        It also determines at what stage you lose customers.
    """,

    'author': "Neuron",
    'website': "https://neuron-systems.com",

    'category': 'Sales/CRM',
    'version': '17.0.1.0.0',

    'license': 'LGPL-3',

    'depends': [
        'base',
        'crm',
    ],

    'data': [
        'views/crm_lead_views.xml',
        'views/views.xml',
        'views/templates.xml',
        # 'security/ir.model.access.csv',  # Uncomment when you define your access rights
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            # Example: 'neuron/static/src/js/script.js',
        ],
        'web.assets_qweb': [
            # Example: 'neuron/static/src/xml/template.xml',
        ],
    },

    'images': ['static/description/icon.png'],

    'application': True,
    'installable': True,
}