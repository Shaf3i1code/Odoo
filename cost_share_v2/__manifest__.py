# -*- coding: utf-8 -*-
{
    'name': "cost_sharing_v2",
    'version': '18.0.0.1',
    'summary': """
        Make Cost Share Fixed Again""",

    'description': """
        By Editing mrp and stock move
    """,

    'author': "Mohanad Elshafei",
    'company': "infotix",
    'website': "https://www.linkedin.com/in/mohandelshafei/",
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    'price': 200,
    'currency': 'USD',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'mrp_account_enterprise', 'purchase_mrp' ,'documents', 'mrp_plm'],

    # always loaded
    'data': [
        # 'report/mrp_cost_structure_report.xml',
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
