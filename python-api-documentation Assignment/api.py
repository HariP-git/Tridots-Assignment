import frappe
from frappe.query_builder import DocType


@frappe.whitelist()
def process_orders():



    Order = DocType("order info")
    Customer = DocType("customer info")

    orders = (
        frappe.qb
        .from_(Order)
        .join(Customer)
        .on(Order.customer == Customer.name)
        .select(
            Order.name,
            Order.status,
            Order.grant_total,
            Customer.customer_name,
            Customer.phone_no
        )
        .where(Order.status == "Pending")
        .run(as_dict=True)
    )



    if orders:
        order_doc = frappe.get_doc(
            "order info",
            orders[0]["name"]
        )

        order_doc.status = "Preparing"

        order_doc.save()


    for order in orders:
        frappe.db.set_value(
            "order info",
            order["name"],
            "status",
            "Completed"
        )


    return {
        "message": "Orders processed successfully",
        "total_orders": len(orders),
        "orders": orders
    }