import mysql.connector

prod_con = mysql.connector.connect(host="localhost", user="root", password="", database="OnlineSeller")
curs1 = prod_con.cursor()


command = "INSERT INTO MC VALUES(%s, %s, %s)"
vals = [
    ("OnePlus Bullets Bluetooth Wireless Z Bass Edition in Ear Earphones", "The Bass Edition comes equipped with Bluetooth v5.0, fully compatible with all smartphones.", 1999),
    ("Portronics Laptop Cooling Stand Wood Portable Laptop Table", "It is a portable laptop stand with cooling fan. If you are looking for multi utility laptop desk, then this product is the best choice", 1899),
    ("Micro USB OTG Cable for Tablets and Mobiles","This cable is made from high quality material and is extremely durable.",499),
    ("SAMSUNG Galaxy Z Fold3 5G","12 GB RAM | 256 GB ROM, 19.3 cm (7.6 inch) WXGA Display", 149999),
    ("SAMSUNG Galaxy S10 ","8 GB RAM | 512 GB ROM | Expandable Upto 512 GB",92000),
    ("Samsung Galaxy Z Series Flip3 5G","17.08 cm (6.7 inch) Full HD+ 2640 x 1080 Main Display",88999),
    ("Apple iPhone 13 Pro Max (Graphite, 512 GB)","512 GB ROM,17.02 cm (6.7 inch) Super Retina XDR Display",159900),
    ("Apple iPhone 11 Pro Max (Space Grey, 64 GB)","64 GB ROM,16.51 cm (6.5 inch) Super Retina XDR Display",117000),
    ("Apple iPhone 12 Pro Max (Pacific Blue, 128 GB)","128 GB ROM,17.02 cm (6.7 inch) Super Retina XDR Display",119900),
    ("SAMSUNG GALAXY M31","64MP + 8MP + 5MP + 5MP rear camera | 32MP front facing camera",16999)
]

curs1.executemany(command, vals)


command = "INSERT INTO TAE VALUES(%s, %s, %s)"
vals = [
    ("AmazonBasics 109 cm 43 inches 4K Ultra HD Smart LED Fire TV AB43U Black","Brand-approved installation at the time of delivery.",23999),
    ("Redmi 80 cm (32 inches) HD Ready Smart LED TV | L32M6-RA (Black) (2021 Model)","supported : Netflix, amazon prime, youtube and internet explorer", 20999),
    ("Mi 100 cm (40 inches) Horizon Edition Full HD Android LED TV 4A", "includes internet access, Disney+hotstar, play store and many more", 18999),
    ("6.5 kg Fully-Automatic Top Load Washing Machine", "Fully-automatic top washing machine for best wash quality along with Energy and Water saving", 11899),
    ("LG superfast frontloading washing machine SEKY674S", "Half an hour wash, perfect for whites, Water saving capacity", 15199),
    ("JABRA evolve stereo headphones", "Bluetooth connected, extra wire also available, 18 months warranty", 8999)
]
curs1.executemany(command, vals)


command = "INSERT INTO SFBL VALUES(%s, %s, %s)"
vals = [
    ("nike men neon collection yking running shoes", "specially designed for rough terrain and feetcare", 10500),
    ("american tourister red cabin suitcase","stylish design with flexible body and attached lock",4899),
    ("yoga mat 2x6 feet blue/pink","soft sponge, fit for outdoor use and washable",999),
    ("dumbbells 2x1kg,2x2kgs,2x5kgs","easy to store, not to be used by children below age 12",2299),
    ("adidas sports bag 4 layer","long-lasting, Black, 29x20x6cm",3499),
    ("proteinex protein shake powder 6 lts","contains egg and milk extracts, extra protein and vitamins b12 and b14",1099)
]
curs1.executemany(command, vals)


command = "INSERT INTO BHG VALUES(%s, %s, %s)"
vals = [
    ("Forever Flawless Constellation Eyeshadow Palette", "Multicoloured,longlasting", 1299),
    ("Renee,Fab 5 5in1 Lipstick 7.5g", "Long Lasting,matte lipstick", 899),
    ("Biotique,Bio Wheat Germ Youthful Nourishing Night Sustainable Cream 50g","Deep Nourishment cream, Almond oil",2899),
    ("Mamaearth,Ubtan Skin Lightening & Brightening Sustainable Face Mask 100 ml","100% natural ingredients", 499),
    ("Mamaearth, Sustainable Onion Hair Fall Control Shampoo 250 ml","Onion Hair Fall Control Shampoo",200),
    ("savlon sanitizers","Guaranteed to kill 99.9% germs",88999),
    ("colgate toothpaste","Active salt with lime freshness.",100),
    ("India Gate (1kg)","Basmathi, unpolished",699),
    ("aashirvaad Atta ","100% wheat 0% maida, extremely nutritious",800)
]
curs1.executemany(command, vals)

command = "INSERT INTO MFWF VALUES(%s, %s, %s)"
vals = [
    ("nike men neon collection jersey (yellow/white/black/grey/blue)", "machine wash, sweat absorbing, can be used as formals", 899),
    ("levis men’s jeans (blue/black/white)","cowboy cut and body hugging styles",2899),
    ("women's cotton front open self design cardigan shrug","black/off white,S/M/XL",2999),
    ("unisex cloudfoam daily wear footware ","washable,black/sky blue/lavender/grey",1299),
    ("oakley holbrook xl sunglasses for men","rectangular,black/brown/blue lenses",7499),
    ("mont blanc crystal fit watch","black with silver,adjustable linked strap",1099)
]
curs1.executemany(command, vals)


command = "INSERT INTO CMI VALUES(%s, %s, %s)"
vals = [
    ("Repair Kit for Car and Bike", "Gilary || Tubeless Tyre Puncture Repair Kit for Car and Bike ((Tubeless Tyre Repair Kit))", 399),
    ("Kanya Car Cleaning Accessories Kit", "Combo Pack,3Pcs Microfiber Cloth/Tiny Duster/Wiper/Sponge/2 Pcs Windshield Cleaning", 569),
    ("Full face Helmet","Sun resistant helmet, very durable",1899),
    ("Protection windscreen","Gear Up A3 Unbreakable Polycarbonate with UV Ray Protection Windscreen",499),
    ("Rain-X RX11806D Washer Fluid Additive (500 ml)","Windshield spray",648),
    ("Seat cover","Pure Leather material",1899),
    ("Car freshener","Lavender flavor",1499),
    ("Car speakers","HIgh music quality",2499)
]
curs1.executemany(command, vals)

command = "INSERT INTO B VALUES(%s, %s, %s)"
vals = [
    ("the hobbit and lord of the rings trilogy", "by J.R.R Tolkein", 999),
    ("The Merchant of Venice","by Shakespere”",999),
    ("Sapiens: a brief history of mankind","by Yuval Noah Harari",499),
    ("Tryst with Destiny","Paul Dettman",299),
    ("Pride and prejudice","Jane austin",499),
    ("three men in a boat","Jerome k Jerome",149)
]
curs1.executemany(command, vals)


command = "INSERT INTO HKP VALUES(%s, %s, %s)"
vals = [
    ("CRAZE CULTURE Fish Hanging", "Handmade Hand-Painted Latkan Toran Garden Decoration Living Room Balcony Indoor Outdoor Wall", 319),
    ("Dinner set", "Amazing Designs and full set available", 5089),
    ("Heater","Overheating protection",3899),
    ("Gaming chairs","2 years warranty",1499),
    ("dog bone and cradle combo","weighs upto 35kgs",3499)
]
curs1.executemany(command, vals)


prod_con.commit()