# -*- coding: utf-8 -*-
{
    'name': "Neuron",

    'summary': "Interactive Phone Script Assistant",
    'description': """
        The script assistant is a universal assistant in which you can program all the options
        for developing a conversation for your managers. A tool that leads the manager automatically
        to a deal with a client. It also determines at what stage you lose customers.
    """,

    'author': "Neuron",
    'website': "https://neuron-systems.com",

    'category': 'Sales/CRM',
    'version': '1.0',

    'license': 'LGPL-3',

    'depends': ['base', 'crm'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            # Пример, если у вас есть JS/CSS
            # 'neuron/static/src/js/neuron.js',
            # 'neuron/static/src/css/neuron.css',
        ],
        'web.assets_qweb': [
            # 'neuron/static/src/xml/neuron_templates.xml',
        ],
    },

    'images': ['static/description/icon.png'],

    'installable': True,
    'application': True,
    'auto_install': False,
}