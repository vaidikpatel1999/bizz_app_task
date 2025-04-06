{
    "name": "Bizzapp Task",
    "version": "17.0.1.0.0",
    "summary": "Bizzapp Task",
    "author": "Vaidik - Radadiya",
    "website": "https://www.bizzappdev.com/",
    "category": "Task",
    "depends": ["sale","base", "stock", "mrp", "contacts", "product""purchase"],
    "data": [
        'data/mail_template.xml',
        "data/notify_sale_person.xml",
        "views/stock_picking_view.xml",
        "views/sale_view_inherite.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
