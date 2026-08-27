// // Copyright (c) 2026, Hari prasath and contributors
// // For license information, please see license.txt

// frappe.query_reports["report2"] = {
// 	filters: [
// 		// {
// 		// 	"fieldname": "my_filter",
// 		// 	"label": __("My Filter"),
// 		// 	"fieldtype": "Data",
// 		// 	"reqd": 1,
// 		// },
// 	],
// };

frappe.query_reports["report2"] = {
  filters: [
    {
      fieldname: "product",
      label: "Product",
      fieldtype: "Data",
    },

    {
      fieldname: "discount_applied",
      label: "Discount Applied",
      fieldtype: "Select",
      options: "\nYes\nNo",
    },
  ],
};
