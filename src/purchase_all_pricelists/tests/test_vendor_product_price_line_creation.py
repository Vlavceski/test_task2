from odoo.tests import TransactionCase


class TestVendorProductPriceView(TransactionCase):

    def setUp(self):
        super().setUp()
        self.partner = self.env['res.partner'].create({
            'name': 'Test Vendor',
        })
        self.product_tmpl = self.env['product.template'].create({
            'name': 'Test Product',
        })
        self.supplierinfo = self.env['product.supplierinfo'].create({
            'partner_id': self.partner.id,
            'product_tmpl_id': self.product_tmpl.id,
            'price': 100.0,
        })

    def test_vendor_product_price_line_creation(self):
        """Test that a vendor product price line is created properly."""
        supplierinfo = self.supplierinfo
        self.assertEqual(supplierinfo.partner_id.name, 'Test Vendor')
        self.assertEqual(supplierinfo.product_tmpl_id.name, 'Test Product')
        self.assertEqual(supplierinfo.price, 100.0)

    def test_vendor_product_price_view_action(self):
        """Test that the vendor product price tree view action works."""
        action = self.env.ref('purchase_all_pricelists.action_vendor_product_price_list').read()[0]
        self.assertEqual(action['res_model'], 'product.supplierinfo')
        self.assertEqual(action['view_mode'], 'tree,form')
