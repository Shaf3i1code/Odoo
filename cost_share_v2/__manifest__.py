# -*- coding: utf-8 -*-
{
    'name': "Cost Sharing ",
    'version': '18.0.0.1',
    'summary': """
        Easily assign exact cost values to byproducts in Manufacturing Orders.""",

    'description': """
This module allows manufacturing teams to assign exact total cost values to byproducts in a Manufacturing Order (MO),
replacing Odoo's default percentage-based cost sharing system.

Instead of using fixed percentages, users can manually input the actual monetary value of each byproduct. 
The module then calculates the unit cost automatically based on the produced quantity.

Key Features:
- Manually assign total cost for each byproduct (e.g., $5 for 5 kg)
- Automatically computes unit cost (e.g., $1 per kg)
- No need to modify the Bill of Materials for cost updates
- Integrated directly into the Manufacturing Order screen
- Enables real-time revaluation without complex configuration
- Improves cost accuracy and transparency in inventory valuation

Ideal for:
- Factories working with volatile byproduct pricing
- Industries like food processing, chemicals, or packaging
- Any production environment needing flexible cost allocation
    """,

    'author': "Mohanad Elshafei",
    'company': "infotix",
    'website': "https://www.linkedin.com/in/mohandelshafei/",
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    'price': 100,
    'currency': 'USD',
    'images': ['static/description/icon.png','static/description/cover.jpg','static/description/screenshot1.png','static/description/screenshot2.png'],

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
