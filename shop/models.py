from django.db import models

# Create your models here.
class ProductBrand(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255,unique=True,default='')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product brands"

class ProductApplication(models.Model):
    name = models.CharField(max_length=250)   
    slug = models.SlugField(max_length=255,unique=True,default='')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Applications"

class ProductCategory(models.Model):
    name = models.CharField(max_length=250)   
    slug = models.SlugField(max_length=255,unique=True,default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Product categories"


class ProductSubCategory(models.Model):
    name = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=255,unique=True,default='')  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product sub categories"


class Supplier(models.Model):
    name = models.CharField(max_length=250)   
    slug = models.SlugField(max_length=255,unique=True,default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Suppliers"

class FulfilmentPartner(models.Model):
    name = models.CharField(max_length=250)   
    slug = models.SlugField(max_length=255,unique=True,default='')
    class Meta:
        verbose_name_plural = "Fulfilment partners"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255,unique=True,default='')
    short_desc=models.TextField(max_length=200,default='')
    long_desc=models.TextField(max_length=1000,default='')
    list_price=models.FloatField(default=0)
    selling_price=models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='productimages/%Y/%m/%d/',null=True)
    image2 = models.ImageField(upload_to='productimages/%Y/%m/%d/',null=True,blank=True)
    image3 = models.ImageField(upload_to='productimages/%Y/%m/%d/',null=True,blank=True)
    image4 = models.ImageField(upload_to='productimages/%Y/%m/%d/',null=True,blank=True)

    brand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,related_name='category',null=True)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='category',null=True)
    subcategory1 = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,related_name='subcategory1',null=True)
    subcategory2 = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,related_name='subcategory2',null=True,blank=True)
    subcategory3 = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,related_name='subcategory3',null=True,blank=True)
    subcategory4 = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,related_name='subcategory4',null=True,blank=True)
    subcategory5 = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,related_name='subcategory5',null=True,blank=True)
    subcategory6 = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,related_name='subcategory6',null=True,blank=True)
    application1 = models.ForeignKey(ProductApplication,on_delete=models.CASCADE,related_name='application1',null=True,blank=True)
    application2 = models.ForeignKey(ProductApplication,on_delete=models.CASCADE,related_name='application2',null=True,blank=True)
    application3 = models.ForeignKey(ProductApplication,on_delete=models.CASCADE,related_name='application3',null=True,blank=True)
    application4 = models.ForeignKey(ProductApplication,on_delete=models.CASCADE,related_name='application4',null=True,blank=True)
    application5 = models.ForeignKey(ProductApplication,on_delete=models.CASCADE,related_name='application5',null=True,blank=True)


    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='supplier',null=True)
    fulfilment_manager = models.ForeignKey(FulfilmentPartner,on_delete=models.CASCADE,related_name='fulfilment_manager',null=True)
    in_stock = models.BooleanField(default = True)
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

    objects = models.Manager() 

