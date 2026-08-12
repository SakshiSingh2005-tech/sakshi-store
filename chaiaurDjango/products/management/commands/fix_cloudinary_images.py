from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Fix Cloudinary image paths for products"

    def handle(self, *args, **kwargs):
        images = [
            "products/Screenshot_2026-08-10_at_1.21.32AM_ha7qjn.png",
            "products/Screenshot_2026-08-10_at_1.26.23AM_kttusd.png",
            "products/Screenshot_2026-08-10_at_1.29.48AM_ixcyoc.png",
            "products/Screenshot_2026-08-10_at_1.31.29AM_nquxu9.png",
            "products/Screenshot_2026-08-10_at_2.34.55AM_njfk9y.png",
            "products/Screenshot_2026-08-10_at_2.36.30AM_fqhyxf.png",
        ]

        products = Product.objects.order_by("id")

        for product, image in zip(products, images):
            product.image.name = image
            product.save(update_fields=["image"])
            self.stdout.write(
                self.style.SUCCESS(
                    f"Product {product.id}: {image}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS("All Cloudinary image paths fixed!")
        )