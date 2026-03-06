from django.db import models

CATEGORY_CHOICES = [
    ('phone',        '📱 Phone'),
    ('laptop',       '💻 Laptop'),
    ('smartwatch',   '⌚ Smart Watch'),
    ('tablet',       '📟 Tablet'),
    ('smartglasses', '🥽 Smart Glasses'),
    ('earbuds',      '🎧 Smart Earbuds'),
    ('smartring',    '💍 Smart Ring'),
]

CONDITION_CHOICES = [
    ('new',         'New'),
    ('used',        'Used'),
    ('refurbished', 'Refurbished'),
]

BRANDS_BY_CATEGORY = {
    'phone': ['Nokia','Ericsson','Siemens','Motorola','BlackBerry','HTC','LG','Sony','Huawei','Lenovo','Apple','Samsung','Xiaomi','Oppo','Vivo','Realme','OnePlus','iQOO','Nothing','Google'],
    'laptop': ['IBM','Compaq','Toshiba','Dell','HP','Lenovo','Acer','Asus','Apple','Microsoft','Razer','MSI','LG','Samsung','Huawei','Honor','Vaio'],
    'smartwatch': ['Pebble','Casio','Fossil','Garmin','Samsung','Fitbit','Huawei','Apple','Google','OnePlus','Amazfit','Noise','boAt','Fire-Boltt','Titan'],
    'tablet': ['BlackBerry','Motorola','HP','Samsung','Amazon','Lenovo','Huawei','Asus','Apple','Microsoft','Xiaomi','Realme','OnePlus','iQOO','Honor'],
    'smartglasses': ['Google','Vuzix','Epson','Intel','Bose','Amazon','Meta','Ray-Ban','Apple','Microsoft','Xiaomi','OPPO','Rokid','Xreal'],
    'earbuds': ['Jabra','Plantronics','Sony','Samsung','Bose','Sennheiser','JBL','Apple','Google','OnePlus','Nothing','boAt','Noise','Realme','Xiaomi','Oppo','Anker','Skullcandy','Amazon'],
    'smartring': ['Motiv','McLear','Oura','Circular','Samsung','Apple','Ultrahuman','RingConn','Evie','Amazfit'],
}

PRODUCTS_BY_BRAND_CATEGORY = {
    'phone::Nokia':['Nokia 3310 (2000)','Nokia 1100','Nokia N95','Nokia Lumia 920','Nokia G60 5G','Nokia XR21'],
    'phone::Ericsson':['Ericsson T28','Ericsson T68','Ericsson W800i'],
    'phone::Siemens':['Siemens A35','Siemens C55','Siemens SL55'],
    'phone::Motorola':['Motorola StarTAC','Moto RAZR V3','Moto G4','Moto G85','Moto Edge 50 Pro','Moto Razr 50 Ultra'],
    'phone::BlackBerry':['BlackBerry Bold 9900','BlackBerry Passport','BlackBerry KEYone','BlackBerry KEY2'],
    'phone::HTC':['HTC Dream','HTC Desire','HTC One M8','HTC 10','HTC U12+'],
    'phone::LG':['LG G2','LG G4','LG V30','LG V60 ThinQ','LG Velvet'],
    'phone::Sony':['Sony Xperia Z','Sony Xperia XZ2','Sony Xperia 5 III','Sony Xperia 1 VI'],
    'phone::Huawei':['Huawei P20 Pro','Huawei Mate 30 Pro','Huawei P50 Pro','Huawei Mate 60 Pro'],
    'phone::Lenovo':['Lenovo A6000','Lenovo K8 Note','Lenovo Legion Phone Duel'],
    'phone::Apple':['iPhone 4','iPhone 6','iPhone X','iPhone 11','iPhone 12','iPhone 13','iPhone 14','iPhone 14 Pro Max','iPhone 15','iPhone 15 Pro','iPhone 15 Pro Max','iPhone 16','iPhone 16 Pro','iPhone 16 Pro Max'],
    'phone::Samsung':['Samsung Galaxy S3','Samsung Galaxy S10','Samsung Galaxy S21','Samsung Galaxy S23','Samsung Galaxy S24','Samsung Galaxy S24 Ultra','Samsung Galaxy Z Fold 6','Samsung Galaxy Z Flip 6','Samsung Galaxy A55'],
    'phone::Xiaomi':['Xiaomi Mi 3','Xiaomi Mi 11','Xiaomi 13 Pro','Xiaomi 14','Xiaomi 14 Ultra','Xiaomi Redmi Note 13 Pro+'],
    'phone::Oppo':['Oppo Find X','Oppo Reno 4','Oppo Find X5 Pro','Oppo Reno 11 Pro','Oppo Find X7 Ultra'],
    'phone::Vivo':['Vivo V5','Vivo X50 Pro','Vivo X90 Pro','Vivo V30 Pro','Vivo X100 Pro'],
    'phone::Realme':['Realme 3 Pro','Realme X2 Pro','Realme GT 2 Pro','Realme 12 Pro+','Realme GT 6'],
    'phone::OnePlus':['OnePlus One','OnePlus 6T','OnePlus 8 Pro','OnePlus 11','OnePlus 12','OnePlus Nord 4'],
    'phone::iQOO':['iQOO 3','iQOO 7','iQOO 11','iQOO 12','iQOO Neo 9 Pro'],
    'phone::Nothing':['Nothing Phone (1)','Nothing Phone (2)','Nothing Phone (2a)','Nothing Phone (2a) Plus'],
    'phone::Google':['Google Nexus 5','Google Pixel 3','Google Pixel 6 Pro','Google Pixel 8','Google Pixel 8 Pro','Google Pixel 9','Google Pixel 9 Pro'],
    'laptop::IBM':['IBM ThinkPad 700C','IBM ThinkPad T40'],
    'laptop::Compaq':['Compaq Presario 700','Compaq Armada M700'],
    'laptop::Toshiba':['Toshiba Satellite A100','Toshiba Portégé R700','Toshiba Tecra Z50'],
    'laptop::Dell':['Dell Inspiron 1525','Dell XPS 13','Dell XPS 15','Dell Latitude 5540','Dell Alienware m16'],
    'laptop::HP':['HP Pavilion 15','HP Spectre x360','HP EliteBook 840','HP Envy 16','HP Omen 16'],
    'laptop::Lenovo':['Lenovo ThinkPad X1 Carbon','Lenovo Legion 5 Pro','Lenovo Yoga 9i','Lenovo ThinkBook 16p'],
    'laptop::Acer':['Acer Aspire 5','Acer Swift 3','Acer Nitro 5','Acer Predator Helios 16'],
    'laptop::Asus':['Asus VivoBook 15','Asus ZenBook 14','Asus ROG Zephyrus G14','Asus ROG Flow X13'],
    'laptop::Apple':['MacBook Pro (2010)','MacBook Air (2013)','MacBook Pro 13 M1','MacBook Air M2','MacBook Pro 14 M3','MacBook Pro 16 M3 Max','MacBook Air 15 M3'],
    'laptop::Microsoft':['Surface Pro 4','Surface Laptop 3','Surface Laptop 5','Surface Pro 10','Surface Laptop Studio 2'],
    'laptop::Razer':['Razer Blade 14','Razer Blade 15','Razer Blade 16','Razer Blade 18'],
    'laptop::MSI':['MSI GE76 Raider','MSI Titan GT77','MSI Prestige 16','MSI Stealth 16 Studio'],
    'laptop::LG':['LG Gram 14','LG Gram 16','LG Gram 17','LG Gram Pro 16'],
    'laptop::Samsung':['Samsung Galaxy Book2 Pro','Samsung Galaxy Book3 Pro 360','Samsung Galaxy Book4 Ultra'],
    'laptop::Huawei':['Huawei MateBook D14','Huawei MateBook X Pro','Huawei MateBook 16s'],
    'laptop::Honor':['Honor MagicBook X 15','Honor MagicBook Pro 16'],
    'laptop::Vaio':['Vaio S13','Vaio SX14','Vaio FE 14'],
    'smartwatch::Pebble':['Pebble Classic (2013)','Pebble Steel','Pebble Time'],
    'smartwatch::Casio':['Casio G-Shock GBD-H1000','Casio Pro Trek WSD-F30'],
    'smartwatch::Fossil':['Fossil Gen 4','Fossil Gen 5','Fossil Gen 6','Fossil Gen 6E'],
    'smartwatch::Garmin':['Garmin Forerunner 235','Garmin Vivoactive 4','Garmin Fenix 7','Garmin Epix Pro'],
    'smartwatch::Samsung':['Samsung Gear S3','Samsung Galaxy Watch','Samsung Galaxy Watch 4','Samsung Galaxy Watch 6','Samsung Galaxy Watch 7','Samsung Galaxy Watch Ultra'],
    'smartwatch::Fitbit':['Fitbit Versa 2','Fitbit Sense','Fitbit Sense 2','Fitbit Versa 4'],
    'smartwatch::Huawei':['Huawei Watch GT 2','Huawei Watch GT 3 Pro','Huawei Watch 4 Pro'],
    'smartwatch::Apple':['Apple Watch Series 3','Apple Watch Series 6','Apple Watch Series 8','Apple Watch Ultra','Apple Watch Series 9','Apple Watch Ultra 2','Apple Watch Series 10'],
    'smartwatch::Google':['Google Pixel Watch','Google Pixel Watch 2','Google Pixel Watch 3'],
    'smartwatch::OnePlus':['OnePlus Watch','OnePlus Watch 2','OnePlus Watch 2R'],
    'smartwatch::Amazfit':['Amazfit Bip','Amazfit GTR 2','Amazfit GTR 4','Amazfit Balance','Amazfit Active 2'],
    'smartwatch::Noise':['Noise ColorFit Pro 3','Noise ColorFit Icon 2','Noise ColorFit Caliber'],
    'smartwatch::boAt':['boAt Storm Pro','boAt Lunar Connect','boAt Wave Leap'],
    'smartwatch::Fire-Boltt':['Fire-Boltt Phoenix','Fire-Boltt Rage','Fire-Boltt Ninja Pro'],
    'smartwatch::Titan':['Titan Smart 2','Titan Stellar'],
    'tablet::BlackBerry':['BlackBerry PlayBook'],
    'tablet::Motorola':['Motorola XOOM'],
    'tablet::HP':['HP TouchPad','HP ElitePad 900'],
    'tablet::Samsung':['Samsung Galaxy Tab S7','Samsung Galaxy Tab S8','Samsung Galaxy Tab S9','Samsung Galaxy Tab S9 Ultra','Samsung Galaxy Tab S9 FE'],
    'tablet::Amazon':['Amazon Fire HD 8','Amazon Fire HD 10','Amazon Fire Max 11'],
    'tablet::Lenovo':['Lenovo Tab M10','Lenovo Tab P12','Lenovo Tab P12 Pro','Lenovo Tab Extreme'],
    'tablet::Huawei':['Huawei MediaPad M5','Huawei MatePad Pro 11','Huawei MatePad Pro 13.2'],
    'tablet::Asus':['Asus ZenPad 3S 10','Asus Vivobook 13 Slate OLED'],
    'tablet::Apple':['iPad (1st gen)','iPad mini 4','iPad Air 3','iPad Air M1','iPad Pro 11 M2','iPad Pro 13 M4','iPad Air 13 M2','iPad mini 7'],
    'tablet::Microsoft':['Microsoft Surface Go','Microsoft Surface Go 3','Microsoft Surface Pro 9','Microsoft Surface Pro 10'],
    'tablet::Xiaomi':['Xiaomi Pad 5','Xiaomi Pad 6','Xiaomi Pad 6 Pro','Xiaomi Pad 6S Pro'],
    'tablet::Realme':['Realme Pad','Realme Pad X','Realme Pad 2'],
    'tablet::OnePlus':['OnePlus Pad','OnePlus Pad Go','OnePlus Pad 2'],
    'tablet::iQOO':['iQOO Pad','iQOO Pad 2'],
    'tablet::Honor':['Honor Pad 8','Honor Pad X9','Honor Pad 9'],
    'smartglasses::Google':['Google Glass Explorer Edition','Google Glass Enterprise Edition 2'],
    'smartglasses::Vuzix':['Vuzix Blade','Vuzix Blade 2','Vuzix Shield'],
    'smartglasses::Epson':['Epson Moverio BT-35E','Epson Moverio BT-45C'],
    'smartglasses::Intel':['Intel Vaunt (2018)'],
    'smartglasses::Bose':['Bose Frames Alto','Bose Frames Tempo','Bose Frames Soprano'],
    'smartglasses::Amazon':['Amazon Echo Frames (2nd gen)','Amazon Echo Frames (3rd gen)'],
    'smartglasses::Meta':['Meta Ray-Ban Stories','Meta Ray-Ban Smart Glasses (2023)'],
    'smartglasses::Ray-Ban':['Ray-Ban Stories','Ray-Ban Meta Wayfarer','Ray-Ban Meta Headliner'],
    'smartglasses::Apple':['Apple Vision Pro'],
    'smartglasses::Microsoft':['Microsoft HoloLens','Microsoft HoloLens 2'],
    'smartglasses::Xiaomi':['Xiaomi Wireless AR Glass Discovery Edition'],
    'smartglasses::OPPO':['OPPO Air Glass','OPPO Air Glass 2','OPPO Air Glass 3'],
    'smartglasses::Rokid':['Rokid Air','Rokid Max','Rokid AR Lite'],
    'smartglasses::Xreal':['Xreal Air','Xreal Air 2','Xreal Air 2 Pro','Xreal One'],
    'earbuds::Jabra':['Jabra Elite 65t','Jabra Elite 85t','Jabra Elite 10','Jabra Elite 4'],
    'earbuds::Plantronics':['Plantronics BackBeat Pro 2','Plantronics BackBeat Fit 3100'],
    'earbuds::Sony':['Sony WF-1000XM3','Sony WF-1000XM4','Sony WF-1000XM5','Sony LinkBuds S'],
    'earbuds::Samsung':['Samsung Galaxy Buds','Samsung Galaxy Buds Pro','Samsung Galaxy Buds 2','Samsung Galaxy Buds 2 Pro','Samsung Galaxy Buds 3 Pro'],
    'earbuds::Bose':['Bose SoundSport Free','Bose QuietComfort Earbuds','Bose QuietComfort Earbuds II'],
    'earbuds::Sennheiser':['Sennheiser Momentum TW 2','Sennheiser Momentum TW 3','Sennheiser Momentum TW 4'],
    'earbuds::JBL':['JBL Free X','JBL Live 300TWS','JBL Tour Pro 2','JBL Tour Pro 3'],
    'earbuds::Apple':['AirPods (1st gen)','AirPods (2nd gen)','AirPods Pro','AirPods (3rd gen)','AirPods Pro 2','AirPods 4'],
    'earbuds::Google':['Google Pixel Buds','Google Pixel Buds Pro','Google Pixel Buds Pro 2'],
    'earbuds::OnePlus':['OnePlus Buds','OnePlus Buds Pro','OnePlus Buds 3','OnePlus Buds 3 Pro'],
    'earbuds::Nothing':['Nothing Ear (1)','Nothing Ear (2)','Nothing Ear (a)','Nothing Ear (open)'],
    'earbuds::boAt':['boAt Airdopes 141','boAt Airdopes 441','boAt Airdopes 800'],
    'earbuds::Noise':['Noise Shots X5 Pro','Noise Buds VS104','Noise Buds Connect 2'],
    'earbuds::Realme':['Realme Buds Air','Realme Buds Air 3','Realme Buds Air 5 Pro'],
    'earbuds::Xiaomi':['Redmi Buds 4 Pro','Xiaomi Buds 4 Pro','Xiaomi Buds 5 Pro'],
    'earbuds::Oppo':['Oppo Enco X','Oppo Enco X2','Oppo Enco Air 3 Pro'],
    'earbuds::Anker':['Anker Soundcore Liberty 3 Pro','Anker Soundcore P40i','Anker Soundcore Liberty 4 NC'],
    'earbuds::Skullcandy':['Skullcandy Indy','Skullcandy Indy Evo','Skullcandy Push Active'],
    'earbuds::Amazon':['Amazon Echo Buds','Amazon Echo Buds (2nd gen)'],
    'smartring::Motiv':['Motiv Ring Gen 1','Motiv Ring Gen 2'],
    'smartring::McLear':['McLear RingPay','McLear RingPay 2'],
    'smartring::Oura':['Oura Ring Gen 1','Oura Ring Gen 2','Oura Ring Gen 3','Oura Ring Gen 4'],
    'smartring::Circular':['Circular Ring Slim','Circular Ring Slim 2'],
    'smartring::Samsung':['Samsung Galaxy Ring'],
    'smartring::Apple':['Apple Smart Ring (rumored)'],
    'smartring::Ultrahuman':['Ultrahuman Ring AIR','Ultrahuman Ring AIR Raw'],
    'smartring::RingConn':['RingConn Smart Ring Gen 1','RingConn Smart Ring Gen 2'],
    'smartring::Evie':['Evie Ring'],
    'smartring::Amazfit':['Amazfit Helio Ring'],
}


class Product(models.Model):
    category     = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    brand        = models.CharField(max_length=100)
    name         = models.CharField(max_length=200)
    model_number = models.CharField(max_length=100, blank=True)
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    condition    = models.CharField(max_length=15, choices=CONDITION_CHOICES, default='new')
    stock        = models.PositiveIntegerField(default=1)
    processor    = models.CharField(max_length=150, blank=True)
    ram          = models.CharField(max_length=50,  blank=True)
    storage      = models.CharField(max_length=50,  blank=True)
    display      = models.CharField(max_length=100, blank=True)
    battery      = models.CharField(max_length=100, blank=True)
    camera       = models.CharField(max_length=150, blank=True)
    os           = models.CharField(max_length=100, blank=True)
    connectivity = models.CharField(max_length=150, blank=True)
    description  = models.TextField(blank=True)
    image        = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} — {self.name}"

    class Meta:
        ordering = ['-created_at']


class Cart(models.Model):
    session_key = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all())

    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_subtotal(self):
        return self.product.price * self.quantity


ORDER_STATUS = [
    ('pending',   'Pending'),
    ('confirmed', 'Confirmed'),
    ('shipped',   'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

class Order(models.Model):
    full_name    = models.CharField(max_length=200)
    phone        = models.CharField(max_length=15)
    email        = models.EmailField(blank=True)
    address      = models.TextField()
    city         = models.CharField(max_length=100)
    pincode      = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status       = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    payment      = models.CharField(max_length=30, default='Cash on Delivery')
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} — {self.full_name}"

    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name     = models.CharField(max_length=200)
    brand    = models.CharField(max_length=100)
    price    = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_subtotal(self):
        return self.price * self.quantity
