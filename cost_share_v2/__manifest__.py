# -*- coding: utf-8 -*-
{
    'name': "Cost Sharing ",
    'version': '18.0.0.1',
    'summary': """
        Make Cost Share Fixed Again""",

    'description': """
        <h2>Manual Cost Sharing for Byproducts in Manufacturing</h2>

<p>
This module enhances Odoo's Manufacturing (MRP) capabilities by allowing users to assign <strong>exact monetary values</strong> to byproducts instead of relying on fixed percentage-based cost shares.
</p>

<h3>🔧 Key Features:</h3>
<ul>
  <li>Define cost share per byproduct using real currency values (e.g., $5, €10).</li>
  <li>Automatically calculates the unit cost based on quantity. Example: if 5 kg of a byproduct is assigned $5, the unit cost becomes $1/kg.</li>
  <li>Improves cost traceability and simplifies re-pricing for future manufacturing orders.</li>
  <li>Eliminates the need to recalculate percentage shares every time product prices change.</li>
</ul>

<h3>🎯 Use Case:</h3>
<p>
Instead of setting cost shares as percentages, you can now specify that 5 units of a byproduct should represent a total of $5. This allows your costing to match actual market or internal valuations, making it easier to update prices when raw material costs fluctuate.
</p>

<h3>📦 Compatibility:</h3>
<ul>
  <li>Odoo 18.0 Enterprise</li>
  <li>Fully integrated with MRP and Inventory modules</li>
</ul>

    """,

    'author': "Mohanad Elshafei",
    'company': "infotix",
    'website': "https://www.linkedin.com/in/mohandelshafei/",
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    'price': 200,
    'currency': 'USD',
    'images': ['static/description/INFOTIX.png'],

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
